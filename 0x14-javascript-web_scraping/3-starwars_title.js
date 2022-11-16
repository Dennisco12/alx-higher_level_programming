#!/usr/bin/node

const request = require('request');
let endPoint = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

endPoint = endPoint + id;
request(endPoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } const content = JSON.parse(body);
  console.log(content.title);
});
