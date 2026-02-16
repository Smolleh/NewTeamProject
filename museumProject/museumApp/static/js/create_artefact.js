

const form = document.getElementById('create-artefact-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        artefactDate:  document.getElementById('artefactDate').value,
        info: document.getElementById('info').value,
        artefactObjectPath: document.getElementById('artefactObjectPath').value
    };

    fetch(`/api/exhibits/${exhibitId}/artefacts/new`, { 
        method: "POST", 
        headers: { 
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()

        },
        body: JSON.stringify(data)
    })

    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to create ");
        }
        return response.json();
    })
    .then(data => { 
        document.getElementById('message').innerText = "Creation saved";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('message').innerText = "Error occured, Creation not save.";
    });


});

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}