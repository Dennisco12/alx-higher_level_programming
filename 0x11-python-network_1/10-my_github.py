#!/usr/bin/python3
"""This takes a github credentials and uses GitHub API to display
the ID"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    token = 'token ' + passwd
    data = {'Authorization': token}
    url = 'https://api.github.com/user'

    r = requests.get(url, data)

    print(r.json().get('id'))
