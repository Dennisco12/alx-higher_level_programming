#!/usr/bin/node

const fs = require('fs');
filePath = process.argv[2];
content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
	if (error) {
		console.log(error); }
});
