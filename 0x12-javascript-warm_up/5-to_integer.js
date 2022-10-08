#!/usr/bin/node

const process = require('process');

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  const ret = 'My number: ' + parseInt(process.argv[2]);
  console.log(ret);
}
