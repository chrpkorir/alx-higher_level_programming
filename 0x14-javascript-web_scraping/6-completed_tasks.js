#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let todoDic;
const countDic = {};
let key;
request(url, errorFunc);

function errorFunc (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    todoDic = JSON.parse(body);
    for (let i = 0; i < todoDic.length; i++) {
      key = todoDic[i].userId;
      if (todoDic[i].completed === true) {
        if (!countDic[key]) {
          countDic[key] = 1;
        } else {
          countDic[key] += 1;
        }
      }
    }
    console.log(countDic);
  }
}
