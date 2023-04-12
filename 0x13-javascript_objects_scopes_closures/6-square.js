#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  constructor (size) {
    super(size);
  }

  charPrint(c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      const line = c.repeat(this.width);
      for (let i = 0; i < this.width; i++) {      
        console.log(line);
      }
    }
  }
}

module.exports = Square;
