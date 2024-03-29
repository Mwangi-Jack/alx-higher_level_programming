#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST
request to the URL with the email as a parameter and
displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    args = sys.argv
    params = {"email": args[2]}

    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')

    req = urllib.request.Request(args[1], data)

    with urllib.request.urlopen(req) as response:
        body = response.read()

        print(body.decode('utf-8'))
