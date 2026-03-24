// creating a new arefact
document.addEventListener("DOMContentLoaded", function() {

    const form = document.getElementById('create-artefact-form')

    form.addEventListener("submit", async function(event) {
        event.preventDefault();

    try {// posting to api endpoint
        const response = await fetch(`/api/exhibits/${exhibitId}/artefacts/new`, {
            method: "POST",
            credentials: "include",
            headers: { "X-CSRFToken": getCSRFToken() },
            body: new FormData(form)
        });
        if (!response.ok) {
            const err = await response.json();
            throw new Error(JSON.stringify(err));
        }
        document.getElementById('message').innerText = "Creation saved";
    } catch (error) {
        console.error("Error:", error);
        document.getElementById('message').innerText = "Error: " + error.message;
    }
});

})

function getCSRFToken()  {
    return document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}

