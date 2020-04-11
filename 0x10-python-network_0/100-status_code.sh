#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl --silent --head 0.0.0.0:5000 | head --lines=1 | cut --delimiter ' ' -f2
