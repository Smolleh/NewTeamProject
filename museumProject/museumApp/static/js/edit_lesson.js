
document.addEventListener("DOMContentLoaded", function() {
    fetch(`/api/exhibits/${exhibitId}/lessonsLearned/edit/${pk}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Data not loaded");
            }
            return response.json();
        })
        
        .then(data => {
            document.getElementById('practicalRecommendations').value = data.practicalRecommendations || '';
            document.getElementById('futureWarnings').value = data.futureWarnings || '';

        })
        .catch(error => console.error(error));
});



const form = document.getElementById('edit-lessons-form')

form.addEventListener("submit", function(event) { 
    event.preventDefault(); 

    const data = { 
        practicalRecommendations: document.getElementById('practicalRecommendations').value,
        futureWarnings:  document.getElementById('futureWarnings').value,
    };

    fetch(`/api/exhibits/${exhibitId}/lessonsLearned/edit/${pk}`, { 
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
        document.getElementById('message').innerText = "Error occured, edit not save.";
    });


});

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}