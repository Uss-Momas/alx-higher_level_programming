#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

const content1 = fs.readFileSync(argv[2], { encoding: 'utf-8', flag: 'r' });
const content2 = fs.readFileSync(argv[3], { encoding: 'utf-8', flag: 'r' });

const content3 = content1 + content2;

fs.writeFileSync(argv[4], content3);
