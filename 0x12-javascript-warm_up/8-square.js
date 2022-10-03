#!/usr/bin/node

const process = require('process');

if (isNaN(parseInt(process.argv[2])) || process.argv[2] = undefined) {
  console.log('Missing size');
} else {
  
