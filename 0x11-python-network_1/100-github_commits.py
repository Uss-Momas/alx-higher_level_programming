#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
"""

import requests
from sys import argv


if __name__ == '__main__':
    repo_name = argv[1]
    own_name = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(own_name,
                                                              repo_name)
    r = requests.get(url)
    for i in range(10):
        sha = r.json()[i].get('sha')
        name = r.json()[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
