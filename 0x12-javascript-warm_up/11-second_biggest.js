#!/usr/bin/node

const process = require('process');

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  let biggest = 0;
  let second = 0;
  let n = 1;
  while (n < parseInt(process.argv.length)) {
    if (parseInt(process.argv[n]) > biggest) {
      second = biggest;
      biggest = parseInt(process.argv[n]);
    } else if (parseInt(process.argv[n]) > second && parseInt(process.argv[n]) < biggest) {
      second = parseInt(process.argv[n]);
    }
    n += 1;
  }
  console.log(second);
}
