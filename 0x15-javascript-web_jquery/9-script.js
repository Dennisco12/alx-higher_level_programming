$.ajax({
	type: 'POST',
	url: 'https://fourtonfish.com/hellosalut/?lang=fr',
	success: (data) => {
		$(DIV#hello).text(data.hello);
	},
	error: () => {
		console.log('Error can\'t load');
	}
});
