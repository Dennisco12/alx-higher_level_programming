#!/bin/bash
#This sends a POST request to the server and displays the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
