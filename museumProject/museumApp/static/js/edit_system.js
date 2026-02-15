
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/exhibits/${exhibitId}/aiSystemDescription/edit/${pk}`) 
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('description').value = data.description || '';
            document.getElementById('purpose').value = data.purpose || '';
            document.getElementById('outputs').value = data.outputs || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-ai-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        description: document.getElementById('description').value,
        purpose:  document.getElementById('purpose').value,
        outputs: document.getElementById('outputs').value
    };

    fetch(`/exhibits/${exhibitId}/aiSystemDescription/edit/${pk}`, { 
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
        response.json();
    })
    .then(data => { 
        document.getElementById('message').innerText = "Edit saved";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('message').innerText = "Error occured, edit not save.";
    });


});

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}