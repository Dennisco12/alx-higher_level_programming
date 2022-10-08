#!/usr/bin/node

const myDict = require('./101-data').dict;
const dictValues = Object.values(myDict).filter((elem, index, self) => self.indexOf(elem) === index);
const newObject = {};
for (let i = 0; i < dictValues.length; i++) {
  const dictKeys = Object.keys(myDict).filter((elem, index) => myDict[elem] === dictValues[i]);
  newObject[dictValues[i]] = dictKeys;
}
console.log(newObject);
