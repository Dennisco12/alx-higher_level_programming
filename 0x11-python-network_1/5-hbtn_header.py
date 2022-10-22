#!/usr/bin/python3
"""This sends a request to the URL and displays the value
of the variable X-Request-Id in the response header"""

from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    content = requests.get(url)

    print(content.headers['X-Request-Id'])
