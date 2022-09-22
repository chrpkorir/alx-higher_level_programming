#!/bin/bash
# cURLrequest that displaythe response body
curl -so /dev/null "$1" -w '%{size_download}\n'
