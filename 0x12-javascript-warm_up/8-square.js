#!/usr/bin/node

const process = require('process');

if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let n = 0;
  let sol = 'X';
  while (n < parseInt(process.argv[2])) {
    sol = sol + 'X';
  } let j = 0;
  while (j < parseInt(process.argv[2])) {
    console.log(sol);
  } }
