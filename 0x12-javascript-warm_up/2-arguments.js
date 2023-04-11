#!/usr/bin/node
// after including package.json { type: "module"}
// form 1 of importing: import { argv } from 'node:process';
// form 2 of importing process, delete the package.json

const process = require('process');
const argv = process.argv;

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
