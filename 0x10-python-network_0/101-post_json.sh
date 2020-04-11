#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl --silent --header "Content-Type: application/json" --request POST --data @"$2" "$1"
