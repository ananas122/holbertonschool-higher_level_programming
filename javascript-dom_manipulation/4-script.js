// Sélectionnez l'élément avec l'id "add_item"
const addItemButton = document.getElementById('add_item');

// Sélectionnez la liste ul avec la classe "my_list"
const myList = document.querySelector('.my_list');

// Ajoutez un gestionnaire d'événement pour le clic sur "add_item"
addItemButton.addEventListener('click', function() {
  // Créez un nouvel élément li
  const newItem = document.createElement('li');
  
  // Définissez le texte item li
  newItem.appendChild(document.createTextNode('Item'));
  
  // Ajoutez le nouvel élément li à la liste ul
  myList.appendChild(newItem);
});
