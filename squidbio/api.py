import requests

from .const import api_url, site_url


def get_seq(seq_url):
    r = requests.get(seq_url.replace(site_url, api_url))
    return r.json()
