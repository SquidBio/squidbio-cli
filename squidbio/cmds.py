from .api import get_seq
from .const import site_url
from .io import make_seq, read_seq
from .linter import lint


def clone_seq(seq_url):
    if site_url not in seq_url or not seq_url.count('/') == 5:
        print('Sequences are identified like {}/[user]/[project][seq_name]'.format(site_url))
        return
    seq = get_seq(seq_url)
    seq_name = seq_url[seq_url.rfind('/') + 1:]
    print('Cloning into {}...'.format(seq_name))
    make_seq(seq, seq_name)
    print('Done!')


def lint_seq(seq_path):
    seq_data = read_seq(seq_path)
    lint(seq_data['seq'])


def config():
    pass
