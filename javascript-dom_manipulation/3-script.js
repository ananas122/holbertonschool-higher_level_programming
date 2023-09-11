// Sélectionnez l'élément avec l'id "toggle_header"
const toggleHeader = document.getElementById('toggle_header');

// Sélectionnez l'élément d'en-tête
const header = document.querySelector('header');

// Ajoutez un gestionnaire d'événement pour le clic sur "toggle_header"
toggleHeader.addEventListener('click', function() {
  // Vérifiez la classe actuelle de l'élément d'en-tête
  if (header.classList.contains('red')) {
    // Si la classe est "red", changez-la en "green"
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList.contains('green')) {
    // Si la classe est "green", changez-la en "red"
    header.classList.remove('green');
    header.classList.add('red');
  }
});
