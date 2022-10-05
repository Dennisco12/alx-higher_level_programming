#!/usr/bin/node

const myList = require('./100-data.js').list;

const newList = myList.map((x, n) => x * n);
console.log(myList);
console.log(newList);
