#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const integer = Number(argv[2]);

function add(a, b) {
  return (a + b);
}

console.log(add(Number(argv[2]), Number(argv[3])));
