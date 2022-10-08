#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0) && (w !== undefined && h !== undefined)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let base = 'X';
    let n = 1;
    while (n < this.width) {
      base = base + 'X';
      n += 1;
    }
    n = 0;
    while (n < this.height) {
      console.log(base);
      n += 1;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
