#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const len = argv.length;

if (len === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
