#!/usr/bin/node
/*
function that executes x times a function.
*/
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
