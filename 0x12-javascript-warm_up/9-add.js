#!/usr/bin/node
/*
script that prints the addition of 2 integers
*/
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

console.log(add(a, b));

function add (a, b) {
  return (a + b);
}
