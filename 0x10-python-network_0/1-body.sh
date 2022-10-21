#!/usr/bin
#This sends a GET request to the URL and displays the body of the response
curl -sI "$1" | grep "200"
