#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl --silent --write-out "%{http_code}\n" "$1" --output /dev/null
