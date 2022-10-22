#!/usr/bin/python3
"""This sends a post request to the URL with email as a parameter"""

import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')

    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as f:
        content = f.read()
        content = content.decode('utf-8')
        print(content)
