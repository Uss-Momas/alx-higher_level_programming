#!/usr/bin/node

const argv = process.argv;
const len = argv.length;
let array = [];
let number = 0;
let second;

if (len <= 3) {
  console.log('0');
} else {
  for (let i = 2; i < len; i++) {
    number = parseInt(Number(argv[i]));
    array.push(number);
  }
  array = array.sort((a, b) => a - b);
  second = array[array.length - 2];
  console.log(second);
}
