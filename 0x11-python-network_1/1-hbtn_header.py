#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the value of the 'X-Request-Id variable found
in the header of the response
"""

import sys
import urllib.request

if __name__ == '__main__':
    args = sys.argv

    with urllib.request.urlopen(args[1]) as response:
        html = response.read()
        print(response.headers.get('X-Request-Id'))
