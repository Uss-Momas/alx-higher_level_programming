#!/usr/bin/node

const argv = process.argv;
const len = argv.length;
let max = 0;
let second = 0;
let number = 0;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  max = Number(argv[2]);
  second = Number(argv[3]);
  for (let i = 2; i < len; i++) {
    number = parseInt(Number(argv[i]));
    if (number >= max) {
      second = max;
      max = number;
    } else if (number >= second) {
      second = number;
    }
  }
  console.log(second);
}
