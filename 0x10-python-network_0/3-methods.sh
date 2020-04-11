#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl --silent --head "$1" | grep Allow | cut --delimiter ' ' -f 2-
