#!/usr/bin/node

const process = require('process');

function add (a, b) {
  return a + b;
}

if (isNaN(process.argv.length < 3)) {
  console.log('NaN');
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  const ret = add(a, b);
  console.log(ret);
}
