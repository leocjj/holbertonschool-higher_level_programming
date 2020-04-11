#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl --silent --header "X-HolbertonSchool-User-Id:98" "$1"
