#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL,
# and displays the response body
curl -s -H "X-School-User-Id: 98" -X GET "$1"
