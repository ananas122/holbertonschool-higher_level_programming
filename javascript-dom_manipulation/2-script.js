// Sélectionnez l'élément avec l'id "red_header"
const redHeader = document.getElementById('red_header');

// Sélectionnez l'élément d'en-tête
const header = document.querySelector('header');

// Ajoutez un gestionnaire d'événement pour le clic sur "red_header"
redHeader.addEventListener('click', function() {
  // Ajoutez la classe "red" à l'élément d'en-tête
  header.classList.add('red');
});
