#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl --silent --head "$1" | grep Allow | cut --delimiter ' ' -f 2-
