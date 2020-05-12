#!/usr/bin/node
const list = require('./100-data').list;

const listMaped = list.map((x, i) => x * i);
console.log(list);
console.log(listMaped);
