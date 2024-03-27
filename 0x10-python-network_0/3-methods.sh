#!/bin/bash
# Displays all the HTTP methods allowed to access the resource
curl -sI $1 | grep Allow
