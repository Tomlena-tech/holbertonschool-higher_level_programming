#!/usr/bin/node
let myVar = process.argv[2];
myVar = parseInt(myVar, 10);
if (Number.isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
