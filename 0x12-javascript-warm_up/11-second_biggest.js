#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.slice(2);
  let nextElement = Number.MIN_VALUE;
  let maxValue = Number.MAX_VALUE;

  arr.forEach(function (element) {
    element = parseInt(element);
    if (element > maxValue) {
      nextElement = maxValue;
      maxValue = element;
    } else if (nextElement < element && maxValue > element) {
      nextElement = element;
    }
  });
  console.log(nextElement);
}
