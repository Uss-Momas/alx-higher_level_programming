#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using package requests
"""
import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
