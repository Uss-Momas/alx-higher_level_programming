#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];
const personUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

let count = 0;
request(url, (err, response, body) => {
  if (err) console.log(err);
  const json = JSON.parse(body).results;
  for (let i = 0; i < json.length; i++) {
    if (json[i].characters.includes(personUrl)) {
      count++;
    }
  }
  console.log(count);
});
