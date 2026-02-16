
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/api/exhibits/${exhibitId}/artefacts/edit/${pk}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('info').value = data.info || '';
            document.getElementById('artefactDate').value = data.artefactDate || '';
            document.getElementById('artefactObjectPath').value = data.artefactObjectPath || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-artefact-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        artefactDate:  document.getElementById('artefactDate').value,
        info: document.getElementById('info').value,
        artefactObjectPath: document.getElementById('artefactObjectPath').value
    };

    fetch(`/api/exhibits/${exhibitId}/artefacts/edit/${pk}`, { 
        method: "PUT", 
        headers: { 
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()

        },
        body: JSON.stringify(data)
    })

    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to save edit");
        }
        return response.json();
    })
    .then(data => { 
        document.getElementById('message').innerText = "Edit saved";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('message').innerText = "Error occured, edit not saved.";
    });


});

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}