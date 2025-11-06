#!/usr/bin/node
let mySquareSize = process.argv[2];
mySquareSize = parseInt(mySquareSize, 10);

if (Number.isNaN(mySquareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < mySquareSize; i++) {
  console.log('X'.repeat(mySquareSize));
  }
}
