#!/usr/bin/python3
"""
Script that taskes in a URL, sends a request to that URL
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    args = sys.argv

    try :
        req = urllib.request.Request(args[1])

        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
