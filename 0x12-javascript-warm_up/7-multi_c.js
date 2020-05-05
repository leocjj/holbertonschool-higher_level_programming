#!/usr/bin/node
/*
script that prints x times “C is fun”
*/
if (Number(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
