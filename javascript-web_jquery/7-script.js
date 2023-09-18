/* global $ */

$(document).ready(function () {
  // Sélectionne l'élément avec l'ID 'character'
  const characterElement = $('#character');

  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Effectue une requête AJAX GET
  $.get(apiUrl, function (data) {
    // Affiche le nom du personnage dans la balise <p> qui a pour ID "name"
    characterElement.text(data.name);
    // Gère les erreurs de la requête AJAX
  }).fail(function (error) {
    console.error(error);
  });
});
