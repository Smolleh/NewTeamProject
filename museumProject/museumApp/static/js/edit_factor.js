// editing contributing factors
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/api/exhibits/${exhibitId}/contributing-factors/edit/`) // load existing data
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('dataIssues').value = data.dataIssues || '';
            document.getElementById('designChoices').value = data.designChoices || '';
            document.getElementById('organisationalOrGovernanceIssues').value = data.organisationalOrGovernanceIssues || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-factors-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { // posting details to db
        dataIssues: document.getElementById('dataIssues').value,
        designChoices:  document.getElementById('designChoices').value,
        organisationalOrGovernanceIssues: document.getElementById('organisationalOrGovernanceIssues').value
    };

    fetch(`/api/exhibits/${exhibitId}/contributing-factors/edit/`, { // posting edit to api endpoint
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