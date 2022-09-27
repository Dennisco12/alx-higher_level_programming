-- This lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
	SELECT tv_genres.id, tv_genres.name
	FROM tv_genres
	LEFT JOIN tv_shows_genres
	ON tv_genres.id = tv_show_genres.genre_id
	LEFT JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_genres.name = 'Comedy'
) AS comedy_id
ON comedy_id.show_id = tv_shows.id
WHERE tv_shows.id = NULL
ORDER BY tv_shows.title ASC
