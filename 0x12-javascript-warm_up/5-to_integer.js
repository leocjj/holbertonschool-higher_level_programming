#!/usr/bin/node
/*
script that prints two arguments passed to it, in the following format: “ is ”
*/
if (Number(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
