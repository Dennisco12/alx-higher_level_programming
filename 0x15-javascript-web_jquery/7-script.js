$.ajax({
	type: 'GET',
	url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
	success: (data) {
		$('DIV#character').text(data.name)
	}
})
