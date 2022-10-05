#!/usr/bin/node

const Squares = require('./5-square');
module.exports = class Square extends Squares {
  charPrint (c) {
    let base;
    if (c === undefined) {
      c = 'X';
    }
    base = c;
    let n = 1;
    while (n < this.height) {
      base = base + c;
      n += 1;
    }
    n = 0;
    while (n < this.width) {
      console.log(base);
      n += 1;
    }
  }
};
