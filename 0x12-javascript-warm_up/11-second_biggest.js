#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments.
*/
const integers = [];
const argumentsNumber = process.argv.length;

if (argumentsNumber <= 2) {
  console.log(0);
} else if (argumentsNumber === 3) {
  console.log(0);
} else {
  for (let i = 2; i < argumentsNumber; i++) {
    integers.push(parseInt(process.argv[i]));
  }
  integers.sort(function (a, b) { return b - a; });
  console.log(integers[1]);
}
