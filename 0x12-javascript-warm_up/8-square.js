#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const integer = Number(argv[2]);

if (!isNaN(integer)) {
  const array = [];
  for (let i = 0; i < parseInt(integer); i++) {
    array.push('X');
  }
  for (let i = 0; i < parseInt(integer); i++) {
    console.log(array.join(''));
  }
} else {
  console.log('Missing size');
}
