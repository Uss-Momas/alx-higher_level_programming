#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const integer = Number(argv[2]);

if (!isNaN(integer)) {
  for (let i = 0; i < parseInt(integer); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
