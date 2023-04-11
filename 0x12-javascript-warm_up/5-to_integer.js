#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const integer = Number(argv[2]);

if (!isNaN(integer)) {
  console.log('My number: ' + parseInt(integer));
} else {
  console.log('Not a number');
}
