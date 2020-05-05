#!/usr/bin/node
/*
script that computes and prints a factorial
*/
const a = parseInt(process.argv[2]);

if (a) {
  console.log(factorial(a));
} else {
  console.log(1);
}

function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return (factorial(a - 1) * a);
  }
}
