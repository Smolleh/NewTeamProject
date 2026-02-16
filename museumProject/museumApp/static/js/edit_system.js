
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/api/exhibits/${exhibitId}/ai-system-description/edit/`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('systemDescription').value = data.systemDescription || '';
            document.getElementById('systemPurpose').value = data.systemPurpose || '';
            document.getElementById('systemOutputs').value = data.systemOutputs || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-ai-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        systemDescription: document.getElementById('systemDescription').value,
        systemPurpose:  document.getElementById('systemPurpose').value,
        systemOutputs: document.getElementById('systemOutputs').value
    };

    fetch(`/api/exhibits/${exhibitId}/ai-system-description/edit/`, { 
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