#!/usr/bin/node
/*
script that prints x times “C is fun”
*/
let x = '';
const times = Number(process.argv[2]);

if (times) {
  for (let i = 0; i < times; i++) {
    x += 'X';
  }
  for (let j = 0; j < times; j++) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
