#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib
from urllib import request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(req) as res:
        try:
            page = res.read()
            print(str(page, 'utf-8'))
        except urllib.error.HTTPError as e:
            print("Error code: " + e.code)
