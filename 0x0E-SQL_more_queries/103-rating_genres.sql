-- This lists all genres in the database hbtn_0d_tvshows_rate by their ratings

SELECT tv_genres.name AS name, SUM(tv_show_ratings.rate) AS total
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY name
ORDER BY total DESC
