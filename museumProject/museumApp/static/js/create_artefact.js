document.addEventListener("DOMContentLoaded", function() {

    const form = document.getElementById('create-artefact-form')

    form.addEventListener("submit", function(event) { 
        event.preventDefault(); 

        const formData = new FormData();

            formData.append('artefactDate', document.getElementById('artefactDate').value);
            formData.append('info', document.getElementById('info').value);
            //formData.append('artefactObjectPath', document.getElementById('artefactObjectPath').value);

        const imageFile = document.getElementById('artefactObjectPath').files[0];
        if (imageFile) {
            formData.append('artefactObjectPath', imageFile);
        }
        fetch(`/api/exhibits/${exhibitId}/artefacts/new`, { 
            method: "POST", 
            headers: { 
                //"Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()

            },
            body: formData
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
            document.getElementById('message').innerText = "Error occured, Creation not saved.";
        });


    });

})

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}