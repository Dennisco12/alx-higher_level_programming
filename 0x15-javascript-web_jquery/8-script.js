$.ajax({
	type: 'GET',
	url: 'https://swapi-api.hbtn.io/api/films/?format=json',
	success: (data) => {
		$.each (data.results, (i, movie) => {
			$('UL#list_movies').append('<li>' + movie.title + '</li>');
		})
	}
});
