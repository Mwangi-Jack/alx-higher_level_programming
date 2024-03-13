#!/usr/bin/node

const args = process.argv.slice(2);

const num = parseInt(args[0]);

function fact (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  }
  return a * fact(a - 1);
}

console.log(fact(num));
