// Sélectionnez l'élément avec l'id "red_header"
const redHeader = document.getElementById('red_header');

// Sélectionnez le header
const header = document.querySelector('header');

// Ajoutez un gestionnaire d'événement pour le clic sur "red_header"
redHeader.addEventListener('click', function() {
  // Changez la couleur du texte de l'en-tête en rouge
  header.style.color = '#FF0000';
});

