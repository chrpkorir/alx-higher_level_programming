#!/bin/bash
# cURL request that display  the size of the response body 
curl -so /dev/null "$1" -w '%{size_download}\n'
