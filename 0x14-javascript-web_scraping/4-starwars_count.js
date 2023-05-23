#!/usr/bin/node

const request = require('request');
// const process = require('process');
// const url = process.argv[2];
const personUrl = 'https://swapi-api.alx-tools.com/api/people/18';

request(personUrl, (err, response, body) => {
  if (err) console.log(err);
  const json = JSON.parse(body);
  console.log(json.films.length);
});
