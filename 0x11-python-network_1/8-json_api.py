#!/usr/bin/python3
"""This takes in a letter and POST request to the url with the letter
as the parameter"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    letter = {'q': q}
    r = requests.post(url, letter)

    try:
        r = r.json()
        if not r:
            print('No result')
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except Exception:
        print("Not a valid JSON")
