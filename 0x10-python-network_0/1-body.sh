#!/bin/bash
#Sends a GET request and displays the body of the response
curl -s $1 | awk '/^$/ {p = 1; next} p'
