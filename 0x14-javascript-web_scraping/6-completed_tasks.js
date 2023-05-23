#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.log(err);
  const json = JSON.parse(body);
  let count = 0;
  const resp = {};
  for (let i = 1; i <= 10; i++) {
    for (let j = 0; j < json.length; j++) {
      if (json[j].userId === i) {
        if (json[j].completed === true) {
          count++;
        }
      }
    }
    resp[i] = count;
    count = 0;
  }
  console.log(resp);
});
