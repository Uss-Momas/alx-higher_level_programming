#!/usr/bin/node

const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const json = JSON.parse(body);
  console.log(json.title);
});
