#!/usr/bin/env node
const process = require('process');
const integer = parseInt(Number(process.argv[2]));

if (!isNaN(integer)) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
