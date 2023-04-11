#!/usr/bin/node

const argv = process.argv;
const number = parseInt(Number(argv[2]));

function factorial (n) {
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

if (isNaN(number)) {
  console.log(factorial(1));
} else {
  console.log(factorial(number));
}
