document.addEventListener("DOMContentLoaded", function() {


    const form = document.getElementById('create-exhibit-form')

    form.addEventListener("submit", function(event) { 
        event.preventDefault(); 
    
        const data = { 
            title: document.getElementById('title').value,
            domain:  document.getElementById('domain').value,
            backgroundDeploymentContext: document.getElementById('backgroundDeploymentContext').value,
            intendedUse: document.getElementById('intendedUse').value
        };
    
        fetch(`api/exhibits/viewCreate`, { 
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
    
    
});
    
function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}