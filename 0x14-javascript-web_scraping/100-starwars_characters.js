#!/usr/bin/node

const request = require('request');
const process = require('process');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (error, resp, bd) => {
        if (error) console.log(error);
        const char_name = JSON.parse(bd).name;
        console.log(char_name);
      });
    }
  }
});
