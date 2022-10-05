#!/usr/bin/node

exports.esrever = function (list) {
  let new_list = [];
  let n = 0;
  for (i = list.length - 1; i >= 0; i--) {
    new_list[n] = list[i];
    n += 1;
  }
  return new_list
}
