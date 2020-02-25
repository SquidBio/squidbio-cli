import json
import os
import requests
from pathlib import Path

from .const import api_url, site_url


def get_api_key():
    home = str(Path.home())
    config_path = '{}/.squidbio/config.json'
    if os.path.exists(config_path.format(home)):
        with open(config_path.format(home), 'r') as f:
            cfg = json.loads(f.read())
            return cfg.get('api_key')
    return None


def get_seq(seq_url):
    api_key = get_api_key()
    headers = {}
    if api_key:
        headers['Api-Key'] = api_key
    r = requests.get(seq_url.replace(site_url, api_url), headers=headers)
    return r.json()


def get_project(project_url):
    api_key = get_api_key()
    headers = {}
    if api_key:
        headers['Api-Key'] = api_key
    r = requests.get(project_url.replace(site_url, api_url), headers=headers)
    return r.json()


def post_seq(seq_url, path):
    api_key = get_api_key()
    headers = {}
    if api_key:
        headers['Api-Key'] = api_key
    r = requests.post(seq_url.replace(site_url, api_url), headers=headers)
    return r.json()
