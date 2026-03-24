
// extract the quiz ID from the current URL
const pathParts = window.location.pathname.split('/');
const quizId = pathParts[pathParts.indexOf('single_quiz') + 1];

// API endpoints for starting and submitting the quiz
const startUrl = `/quizzes-api/${quizId}/start/`;
const submitUrl = `/quizzes-api/${quizId}/submit/`;


let selectedAnswers = {};


// if the quiz has already been completed previous result shown
async function loadQuiz() {
    const response = await fetch(startUrl, {
        credentials: 'include'
    });

    if (!response.ok) {
        document.getElementById('quiz-title').innerText = "Failed to load quiz";
        return;
    }

    const data = await response.json();

    // if user has a score, they have already completed quiz
    if (data.score !== undefined) {
        document.getElementById('quiz-title').innerText = "You have already completed this quiz!";
        document.getElementById('result').innerText = `Your score: ${data.score}%`;
        document.getElementById('points').innerText = `Points earned: ${data.points}`;
        document.getElementById('passed').innerText = data.passed ? 'Result: Passed' : 'Result: Failed';
        document.getElementById('submit').style.display = 'none';
        return;
    }

    // render the quiz title and clear any existing question content
    document.getElementById('quiz-title').innerText = data.quiz_name;
    const container = document.getElementById("quiz");
    container.innerHTML = "";

    // builds DOM block for each question
    data.questions.forEach((q, index) => {
        const qDiv = document.createElement("div");
        qDiv.classList.add("question");

        const qText = document.createElement("p");
        qText.innerText = `${index + 1}. ${q.question_text}`;
        qDiv.appendChild(qText);

        const aDiv = document.createElement("div");
        aDiv.classList.add("answers");

        // create a radio button for each answer
        q.answers.forEach(a => {
            const label = document.createElement("label");
            const radio = document.createElement("input");
            radio.type = "radio";
            radio.name = `question_${q.id}`;
            radio.value = a.id;
            // records the answer when the user clicks button
            radio.addEventListener("change", () => {
                selectedAnswers[q.id] = a.id;
            });
            label.appendChild(radio);
            label.appendChild(document.createTextNode(a.answer_text));
            aDiv.appendChild(label);
            aDiv.appendChild(document.createElement("br"));
        });

        qDiv.appendChild(aDiv);
        container.appendChild(qDiv);
    });
}

// submits the user's selected answers to the API and displays the result.
async function submitQuiz(e) {
    e.preventDefault();

    // build the submission payload
    const payload = {
        answers: Object.entries(selectedAnswers).map(([qId, aId]) => ({
            question_id: parseInt(qId),
            answer_id: parseInt(aId)
        }))
    };

    const response = await fetch(submitUrl, {
        method: "PATCH",
        credentials: 'include',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken')
        },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {
        document.getElementById('result').innerText = "Submission failed. Please try again.";
        return;
    }

    // displays the score, points, and pass/fail result
    const result = await response.json();
    document.getElementById('result').innerText =`You answered ${result.correct} out of ${result.total} correctly. Score: ${result.score.toFixed(1)}%`;
    document.getElementById('points').innerText = `Points earned: ${result.points}`;
    document.getElementById('passed').innerText = result.passed ? 'Result: Passed' : 'Result: Failed';

    // prevents resubmission
    document.getElementById('submit').disabled = true;
    document.querySelectorAll('#quiz input[type="radio"]').forEach(r => r.disabled = true);
}


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// attach submit handler
document.getElementById('quiz-form').addEventListener('submit', submitQuiz);

loadQuiz();