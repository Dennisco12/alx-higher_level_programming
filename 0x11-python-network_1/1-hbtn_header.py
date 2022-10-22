#!/usr/bin/python3
"""This takes a url, sends the request to the URL and displays the
value of X-request-Id variable"""
from urllib import request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with request.urlopen(url) as f:
        headers = f.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
