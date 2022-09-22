#!/bin/bash
# Sends request to URL argument, and displays response status code
curl "$1" -w '%{http_code}' -so /dev/nul
