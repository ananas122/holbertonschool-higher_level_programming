// Sélectionnez l'élément avec l'id "update_header"
const updateHeaderButton = document.getElementById('update_header');

// Ajoutez un gestionnaire d'événement pour le clic sur "update_header"
updateHeaderButton.addEventListener('click', function() {
  // Mettez à jour le texte de l'en-tête directement
  document.querySelector('header').textContent = 'New Header!!!';
});
