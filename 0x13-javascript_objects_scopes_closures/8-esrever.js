#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let n = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[n] = list[i];
    n += 1;
  }
  return newList;
};
