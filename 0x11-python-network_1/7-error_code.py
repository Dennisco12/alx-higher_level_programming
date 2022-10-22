#!/usr/bin/python3
"""This sends a request to the URL and displays the body of the
response"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        content = requests.get(url)
        content.raise_for_status()
        print(content.text)
    except:
        print("Error code: {}".format(content.status_code))
