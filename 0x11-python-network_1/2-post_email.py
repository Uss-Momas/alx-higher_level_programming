#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        page = response.read()
        print(str(page, 'utf-8'))
