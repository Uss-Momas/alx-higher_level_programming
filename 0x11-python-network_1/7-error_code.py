#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    code = res.status_code
    if code >= 400:
        print('Error code: {}'.format(code))
    else:
        print(res.text)
