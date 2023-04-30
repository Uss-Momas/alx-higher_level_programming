#!/usr/bin/bash
# Bash script that takes in URL and sends GET request to the URL
curl -s -X GET -L "$1"
