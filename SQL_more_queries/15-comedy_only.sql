SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id

-- Filtre les enregistrements en ne sélectionnant que ceux dont le titre de l'émission est 'Dexter'
WHERE tv_genres.name = "Comedy"
ORDER BY tv_genres.name ASC;