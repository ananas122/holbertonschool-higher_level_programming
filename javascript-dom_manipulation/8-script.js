function fetchHelloTranslation () {
  // Sélectionnez l'élément HTML avec l'id "hello"
  const helloElement = document.getElementById('hello');

  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Utilisez l'API Fetch pour récupérer la traduction
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      // Extrait et affiche la traduction
      const helloTranslation = data.hello;
      helloElement.textContent = helloTranslation;
    })
    .catch((error) => {
      console.error('Erreur de fetch :', error);
    });
}

// Appelez la fonction lorsque le document est prêt
document.addEventListener('DOMContentLoaded', fetchHelloTranslation);
