#!/usr/bin/node

const process = require('process');

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

if (process.argv[2] === undefined) {
  console.log('1');
} else {
  const a = process.argv[2];
  const ret = factorial(parseInt(a));
  console.log(ret);
}
