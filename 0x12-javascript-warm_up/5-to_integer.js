#!/usr/bin/env node

const process = require('process');
const argv = process.argv;

const convertedNumber = Number(argv[2]);

if (isNaN(convertedNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(convertedNumber));
}
