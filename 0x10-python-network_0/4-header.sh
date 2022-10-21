#!/bin/bash
#This sends a GET request to the server with a variable
curl -s "$1" -X GET -H "X-School-User-Id: 98"
