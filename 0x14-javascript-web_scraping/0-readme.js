#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const filename = process.argv[2];

try {
  const data = fs.readFileSync(filename, { encoding: 'utf-8', flag: 'r' });
  console.log(data);
} catch (err) {
  console.log(err);
}
