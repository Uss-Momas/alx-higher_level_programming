#!/usr/bin/python3
"""
Python scrip that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

if __name__ == "__main__":
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(str(html, 'utf-8')))
