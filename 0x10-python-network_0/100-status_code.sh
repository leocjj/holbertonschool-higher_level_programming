#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl --output /dev/null --silent --write-out "%{http_code}\n" 0.0.0.0:5000
