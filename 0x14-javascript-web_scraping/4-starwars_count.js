#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

let dicFilms = {};
let count = 0;

request(url, errorFunc);

function errorFunc (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    dicFilms = JSON.parse(body);
    // console.log(dicFilms); // shows all the data
    for (let i = 0; i < dicFilms.results.length; i++) {
      for (let j = 0; j < dicFilms.results[i].characters.length; j++) {
        if (dicFilms.results[i].characters[j].includes('/18/')) {
          count += 1;
        }
      }
      // console.log(dicFilms.results[i]); shows all the results
      // console.log(dicFilms.results[i].characters); show just the characters
    }
    console.log(count);
  }
}
