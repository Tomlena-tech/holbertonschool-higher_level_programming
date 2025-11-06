#!/usr/bin/env node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let second = -Infinity;

  for (const n of args) {
    if (n > max) {
      second = max;
      max = n;
    } else if (n > second && n < max) {
      second = n;
    }
  }

  console.log(second);
}
