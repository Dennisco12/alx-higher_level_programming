#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
	if (error) {
		console.log(error);
	} const content = JSON.parse(body);
	let count = 0;
	for (const items of content.results) {
		for (const item of items.characters) {
			if (item.includes(18)) {
				count++;
		}}}
	console.log(count);
});
