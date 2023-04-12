#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
const list = [];

console.log(dict);
for (const key in dict) {
  // console.log(`${key}: ${dict[key]}`);
  list.push(key);
  newDict[dict[key]] = list;
}

console.log(newDict);
