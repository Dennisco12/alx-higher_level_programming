#!/bin/bash
# This takes a URL and sends a request to that URL, and displays
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
