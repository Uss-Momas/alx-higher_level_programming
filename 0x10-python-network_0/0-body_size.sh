#!/bin/bash
# take in URL sends a request to the URL displays the size of the body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
