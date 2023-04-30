#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    github_api_url = 'https://api.github.com'
    username = argv[1]
    password = argv[2]
    headers = {'Authorization': 'token {}'.format(password),
               'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github+json'
               }

    res = requests.get('{}/user'.format(github_api_url), headers=headers)
    result = res.json().get('id')
    if result:
        print(result)
    else:
        print(None)
