#!/usr/bin/node

const process = require('process');
const argv = process.argv;
let len = 0;
argv.forEach(
  (val, index) => {
    len++;
  }
);
if (len === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
