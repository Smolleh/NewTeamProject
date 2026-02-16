document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('create-factors-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        dataIssues: document.getElementById('dataIssues').value,
        designChoices:  document.getElementById('designChoices').value,
        organisationalOrGovernanceIssues: document.getElementById('organisationalOrGovernanceIssues').value
    };

    fetch(`/api/exhibits/${exhibitId}/contributingFactors/new`, { 
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

})

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}