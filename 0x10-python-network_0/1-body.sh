#!bin/bash
# Bash script that takes in URL and sends GET request to the URL
curl -s "$1" -X GET -L
