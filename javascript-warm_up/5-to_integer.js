#!/usr/bin/node
const Arg = process.argv[2];
if (!isNaN(Arg)) {
console.log ('Not a number');
} else {
  console.log (parseInt(Arg));
}
