/* global $ */

// Make an AJAX GET request to the API URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  // Extract the character name from the response JSON
  const characterName = data.name;
  // Display the character name in the HTML <div id="character">
  $('#character').text(characterName);
});
