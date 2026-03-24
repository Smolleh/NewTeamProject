document.addEventListener("DOMContentLoaded", function () {
    loadQuestions();

    document.getElementById("edit-quiz-form").addEventListener("submit", saveQuizDetails);
    document.getElementById("add-question-btn").addEventListener("click", function () {
        addNewQuestionBlock();
    });
});

function getCSRFToken() {
    return document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="))
        ?.split("=")[1];
}

//loads existing questions

function loadQuestions() {
    fetch(`/quizzes-api/manage/${quizId}/questions/`)
        .then((res) => {
            if (!res.ok) throw new Error("Failed to load questions");
            return res.json();
        })
        .then((questions) => {
            const container = document.getElementById("questions-container");
            container.innerHTML = "";
            questions.forEach((q) => renderExistingQuestion(q));
        })
        .catch(() => {
            document.getElementById("question-message").textContent = "Failed to load questions.";
        });
}

// renders an exisiting question
function renderExistingQuestion(q) {
    const container = document.getElementById("questions-container");
    const block = document.createElement("div");
    block.className = "question-block";
    block.dataset.questionId = q.id;
    // mapping answers to quiz 
    const answersHtml = q.answers
        .map(
            (a) => `
        <div class="answer-row">
            <input type="text" class="answer-text" value="${escapeHtml(a.answer_text)}" required>
            <label><input type="checkbox" class="answer-correct" ${a.is_correct ? "checked" : ""}> Correct</label>
        </div>`
        )
        .join("");
    // html to show questions
    block.innerHTML = `
        <h3>Question</h3>
        <input type="text" class="question-text" value="${escapeHtml(q.question_text)}" required>
        <div class="answers-container">${answersHtml}</div>
        <button type="button" class="add-answer-btn">+ Add Answer</button>
        <button type="button" class="save-question-btn">Save Question</button>
        <button type="button" class="delete-question-btn">Delete Question</button>
        <p class="question-msg"></p>
    `;
    // curator functions to add, save and delete questions
    block.querySelector(".add-answer-btn").addEventListener("click", () =>
        addAnswerRow(block.querySelector(".answers-container"))
    );
    block.querySelector(".save-question-btn").addEventListener("click", () =>
        saveExistingQuestion(block, q.id)
    );
    block.querySelector(".delete-question-btn").addEventListener("click", () =>
        deleteQuestion(block, q.id)
    );

    container.appendChild(block);
}

// saves an existing question

async function saveExistingQuestion(block, questionId) {
    const msg = block.querySelector(".question-msg");
    const questionText = block.querySelector(".question-text").value.trim();
    const answers = collectAnswers(block);
    // confirming length 
    if (answers.length < 2) {
        msg.textContent = "At least 2 answers required.";
        return;
    }

    try { // connecting to endpoint to save to db
        const res = await fetch(`/quizzes-api/manage/question/${questionId}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
            body: JSON.stringify({ question_text: questionText, answers }),
        });
        msg.textContent = res.ok ? "Saved." : "Failed to save.";
    } catch {
        msg.textContent = "Error saving question.";
    }
}

// delete a question 
async function deleteQuestion(block, questionId) {
    if (!confirm("Delete this question?")) return; // confirming action
    try {
        const res = await fetch(`/quizzes-api/manage/question/${questionId}/`, {
            method: "DELETE",
            headers: { "X-CSRFToken": getCSRFToken() },
        });
        if (res.ok || res.status === 204) {
            block.remove();
        } else {
            block.querySelector(".question-msg").textContent = "Failed to delete.";
        }
    } catch {
        block.querySelector(".question-msg").textContent = "Error deleting question.";
    }
}

// add a new question block
function addNewQuestionBlock() {
    const container = document.getElementById("questions-container");
    const block = document.createElement("div");
    block.className = "question-block";
    // curator html form for inputting questions 
    block.innerHTML = `
        <h3>New Question</h3>
        <input type="text" class="question-text" placeholder="Question text" required>
        <div class="answers-container">
            <div class="answer-row">
                <input type="text" class="answer-text" placeholder="Answer text" required>
                <label><input type="checkbox" class="answer-correct"> Correct</label>
            </div>
            <div class="answer-row">
                <input type="text" class="answer-text" placeholder="Answer text" required>
                <label><input type="checkbox" class="answer-correct"> Correct</label>
            </div>
        </div>
        <button type="button" class="add-answer-btn">+ Add Answer</button>
        <button type="button" class="save-question-btn">Save Question</button>
        <button type="button" class="remove-question-btn">Remove</button>
        <p class="question-msg"></p>
    `;

    block.querySelector(".add-answer-btn").addEventListener("click", () =>
        addAnswerRow(block.querySelector(".answers-container"))
    );
    block.querySelector(".save-question-btn").addEventListener("click", () =>
        saveNewQuestion(block)
    );
    block.querySelector(".remove-question-btn").addEventListener("click", () =>
        block.remove()
    );

    container.appendChild(block);
}

// save a new question

async function saveNewQuestion(block) {
    const msg = block.querySelector(".question-msg");
    const questionText = block.querySelector(".question-text").value.trim();
    const answers = collectAnswers(block);

    if (answers.length < 2) {
        msg.textContent = "At least 2 answers required.";
        return;
    }

    try {
        const res = await fetch(`/quizzes-api/manage/${quizId}/questions/`, {
            method: "POST",
            headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
            body: JSON.stringify({ question_text: questionText, answers }),
        });
        if (res.ok) {
            const created = await res.json();
            block.remove();
            renderExistingQuestion(created);
        } else {
            msg.textContent = "Failed to save question.";
        }
    } catch {
        msg.textContent = "Error saving question.";
    }
}

// save quiz metadata

async function saveQuizDetails(event) {
    event.preventDefault();
    const msg = document.getElementById("quiz-message");

    const data = {
        name: document.getElementById("quiz-name").value.trim(),
        topic: document.getElementById("quiz-topic").value.trim(),
        num_questions: parseInt(document.getElementById("quiz-num-questions").value),
        passing_score: parseFloat(document.getElementById("quiz-passing-score").value),
        max_points: parseInt(document.getElementById("quiz-max-points").value),
        exhibit: parseInt(document.getElementById("quiz-exhibit").value),
    };

    try {
        const res = await fetch(`/quizzes-api/manage/${quizId}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
            body: JSON.stringify(data),
        });
        msg.textContent = res.ok ? "Quiz details saved." : "Failed to save quiz details.";
    } catch {
        msg.textContent = "Error saving quiz details.";
    }
}

// helper functions

function addAnswerRow(answersContainer) {
    const row = document.createElement("div");
    row.className = "answer-row";
    row.innerHTML = `
        <input type="text" class="answer-text" placeholder="Answer text" required>
        <label><input type="checkbox" class="answer-correct"> Correct</label>
        <button type="button" class="remove-answer-btn">Remove</button>
    `;
    row.querySelector(".remove-answer-btn").addEventListener("click", () => row.remove());
    answersContainer.appendChild(row);
}
// gets all answers
function collectAnswers(block) {
    const answers = [];
    block.querySelectorAll(".answer-row").forEach((row) => {
        const text = row.querySelector(".answer-text").value.trim();
        if (text) {
            answers.push({
                answer_text: text,
                is_correct: row.querySelector(".answer-correct").checked,
            });
        }
    });
    return answers;
}
// failsafe for html errors 
function escapeHtml(str) {
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}
