#!/bin/bash
# Displays all the HTTP methods allowed to access the resource
curl -sI -X OPTIONS $1 | grep "Allow:" | cut -d " " -f 2-
