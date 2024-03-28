#!/usr/bin/python3

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

with urllib.request.urlopen(req) as response:
    body = response.read()
    print(body)
