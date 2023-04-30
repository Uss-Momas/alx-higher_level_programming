#!/usr/bin/python3
"""
Python scrip that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

req = request.Request('https://alx-intranet.hbtn.io/status')
with request.urlopen(req) as response:
    html = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(html), html, str(html, 'utf-8')))
