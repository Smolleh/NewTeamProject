// editing failure description
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/api/exhibits/${exhibitId}/failure-description/edit/`) // load existing data
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('whatWentWrong').value = data.whatWentWrong || '';
            document.getElementById('howItWasDetected').value = data.howItWasDetected || '';
            document.getElementById('whatWasAffected').value = data.whatWasAffected || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-failure-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { // posting details to db
        whatWentWrong: document.getElementById('whatWentWrong').value,
        howItWasDetected:  document.getElementById('howItWasDetected').value,
        whatWasAffected: document.getElementById('whatWasAffected').value
    };

    fetch(`/api/exhibits/${exhibitId}/failure-description/edit/`, { // posting edit to api endpoint
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
    .then(() => {
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