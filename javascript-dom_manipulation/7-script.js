const movieListElement = document.getElementById('list_movies');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Extract and list the movie titles
    const movies = data.results;
    movies.forEach(movie => {
      // Get the title of the current movie
      const movieTitle = movie.title;
      // Create a new list item element.
      const listItem = document.createElement('li');
      // Set the text content of the list item to the movie title.
      listItem.textContent = movieTitle;
      // Append the list item to the movie list element.
      movieListElement.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error(error);
  });
