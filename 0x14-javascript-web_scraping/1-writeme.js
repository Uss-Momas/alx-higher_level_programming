#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const filename = process.argv[2];
const contentString = process.argv[3];

try {
  fs.writeFileSync(filename, contentString, 'utf-8');
} catch (err) {
  console.log(err);
}
