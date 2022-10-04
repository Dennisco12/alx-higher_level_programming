#!/usr/bin/node

const Square = require('./6-square');
module.exports = class Square extends Square {
  constructor (size) {
    super(size);
  }
  charPrint (c) {
    let base = c;
    let n = 1;
    while (n < this.height) {
      base = base + c;
      n += 1;
    }
    while (n < this.width) {
      console.log(base);
      n += 1;
    }
  }
}
