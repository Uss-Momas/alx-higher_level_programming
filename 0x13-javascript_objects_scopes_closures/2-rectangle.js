#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(isNaN(Number(w)) || isNaN(Number(h)))) {
      if (Number(w) > 0 && Number(h) > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
}

module.exports = Rectangle;
