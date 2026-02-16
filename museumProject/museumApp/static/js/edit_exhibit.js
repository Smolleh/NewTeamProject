
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/api/exhibits/${exhibitId}/edit`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('title').value = data.title || '';
            document.getElementById('domain').value = data.domain || '';
            document.getElementById('backgroundDeploymentContext').value = data.backgroundDeploymentContext || '';
            document.getElementById('intenedUse').value = data.intenedUse || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-exhibit-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        title: document.getElementById('title').value,
        domain:  document.getElementById('domain').value,
        backgroundDeploymentContext: document.getElementById('backgroundDeploymentContext').value,
        intenedUse: document.getElementById('intenedUse').value
    };

    fetch(`/api/exhibits/${exhibitId}/edit`, { 
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