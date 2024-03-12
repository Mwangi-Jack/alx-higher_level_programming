#!/usr/bin/node

const args = process.argv.slice(2);

const arg = (parseInt(args[0]));

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args[0])}`);
}
