#!/usr/bin/node
const myVar1 = process.argv[2];
const myVar2 = process.argv[3];
if (myVar1 === undefined || myVar2 === undefined) {
  console.log('NaN');
} else {
  console.log(Number(myVar1) + Number(myVar2));
}
