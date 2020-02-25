import json
import os
from pathlib import Path

from .api import get_project, get_seq
from .const import seq_types, site_url
from .diff import diff, print_diffs
from .io import make_project, make_seq, read_seq
from .linter import lint


def clone_project(project_url):
    if site_url not in project_url or not project_url.count('/') == 4:
        print('Projects are identified like {}/[user]/[project]'.format(site_url))
        return
    project = get_project(project_url)
    project_name = project_url[project_url.rfind('/') + 1:]
    print('Cloning into {}...'.format(project_name))
    make_project(project, project_name)
    os.chdir(project_name)
    for seq in project.get('Sequences'):
        sk = seq.get('sk')
        seq_name = sk[sk.rfind('/') + 1:]
        clone_seq('{}/{}'.format(project_url, seq_name), silent=True)
    print('Done!')


def clone_seq(seq_url, silent=False):
    if site_url not in seq_url or not seq_url.count('/') == 5:
        print('Sequences are identified like {}/[user]/[project]/[seq_name]'.format(site_url))
        return
    seq = get_seq(seq_url)
    seq_name = seq_url[seq_url.rfind('/') + 1:]
    if not silent:
        print('Cloning into {}...'.format(seq_name))
    make_seq(seq, seq_name)
    if not silent:
        print('Done!')


def lint_seq(seq_path):
    seq_data = read_seq(seq_path)
    lint(seq_data['seq'])


def diff_project(project_path='.'):
    for root, dirs, files in os.walk(project_path):
        for file_name in files:
            ext = file_name[file_name.rfind('.') + 1:]
            if ext == 'json' or ext not in seq_types:
                continue
            diff_seq(os.path.join(root, file_name))


def diff_seq(seq_path):
    seq_data = read_seq(seq_path)
    seq = seq_data['seq']
    slash_idx = seq_path.rfind('/')
    if slash_idx == -1:
        old_seq_path = '.sequence.json'
    else:
        old_seq_path = seq_path[0:slash_idx] + '/.sequence.json'
    old_seq_data = read_seq(old_seq_path)
    old_seq = old_seq_data['Sequence']
    diffs = diff(old_seq, seq)
    has_diff = not all([d[0] == 'equal' for d in diffs])
    if has_diff:
        print(seq_path)
        print_diffs(diffs, old_seq, seq)


def config():
    api_key = input('API key: ')
    cfg = {'api_key': api_key}

    home = str(Path.home())
    Path("{}/.squidbio".format(home)).mkdir(parents=True, exist_ok=True)
    with open('{}/.squidbio/config.json'.format(home), 'w') as f:
        f.write(json.dumps(cfg))
