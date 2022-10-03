#!/usr/bin/node

const process = require('process');
let n = 0;

if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (n < parseInt(process.argv[2])) {
    console.log('C is fun');
    n += 1;
  }
}
