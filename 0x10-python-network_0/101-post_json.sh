#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl --silent --header "Content-Type: application/json" --request POST --data @"$2" "$1"
