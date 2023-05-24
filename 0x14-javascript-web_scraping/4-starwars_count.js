#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

let count = 0;
request(url, (err, response, body) => {
  if (err) console.log(err);
  const json = JSON.parse(body).results;
  for (let i = 0; i < json.length; i++) {
    const characters = json[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].search('18') !== -1) {
        count++;
      }
    }
  }
  console.log(count);
});
