    const characterElement = document.getElementById('character');

    // URL for fetching character data
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    // Use the Fetch API to fetch character data
    fetch(apiUrl)
        // Convert the response to JSON format.
        .then(response => response.json())
        .then(data => {
            // Extract the character name from the data.
            const characterName = data.name;
            // Set the text content of the character element to the character name.
            characterElement.textContent = characterName;
        })
        // Handle any errors that occur during the fetch or JSON conversion process.
        .catch(error => {
            console.error(error);
        });
