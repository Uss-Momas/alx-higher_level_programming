#!/usr/bin/node

exports.converter = function (base) {
  let reminder;

  return function (number){
    reminder = number % base;
    console.log(reminder);
  };
}
