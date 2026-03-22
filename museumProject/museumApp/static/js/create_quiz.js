document.addEventListener("DOMContentLoaded", function () {
    let questionCount = 0;

    document.getElementById("add-question-btn").addEventListener("click", addQuestion);
    document.getElementById("create-quiz-form").addEventListener("submit", submitQuiz);

    function addQuestion() {
        questionCount++;
        const container = document.getElementById("questions-container");

        const block = document.createElement("div");
        block.className = "question-block";
        block.dataset.index = questionCount;
        block.innerHTML = `
            <h3>Question ${questionCount}</h3>
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
            <button type="button" class="remove-question-btn">Remove Question</button>
        `;

        block.querySelector(".add-answer-btn").addEventListener("click", function () {
            addAnswer(block.querySelector(".answers-container"));
        });

        block.querySelector(".remove-question-btn").addEventListener("click", function () {
            block.remove();
        });

        container.appendChild(block);
    }

    function addAnswer(answersContainer) {
        const row = document.createElement("div");
        row.className = "answer-row";
        row.innerHTML = `
            <input type="text" class="answer-text" placeholder="Answer text" required>
            <label><input type="checkbox" class="answer-correct"> Correct</label>
            <button type="button" class="remove-answer-btn">Remove</button>
        `;
        row.querySelector(".remove-answer-btn").addEventListener("click", function () {
            row.remove();
        });
        answersContainer.appendChild(row);
    }

    async function submitQuiz(event) {
        event.preventDefault();
        const msg = document.getElementById("message");
        msg.textContent = "";

        const quizData = {
            name: document.getElementById("quiz-name").value.trim(),
            topic: document.getElementById("quiz-topic").value.trim(),
            num_questions: parseInt(document.getElementById("quiz-num-questions").value),
            passing_score: parseFloat(document.getElementById("quiz-passing-score").value),
            max_points: parseInt(document.getElementById("quiz-max-points").value),
            exhibit: parseInt(document.getElementById("quiz-exhibit").value),
        };

        if (!quizData.exhibit) {
            msg.textContent = "Please select an exhibit.";
            return;
        }

        const questionBlocks = document.querySelectorAll(".question-block");
        if (questionBlocks.length === 0) {
            msg.textContent = "Please add at least one question.";
            return;
        }

        if (quizData.num_questions > questionBlocks.length) {
            msg.textContent = `You have ${questionBlocks.length} question(s) but set the quiz to show ${quizData.num_questions}. Add more questions or lower the number.`;
            return;
        }

        // Step 1: create the quiz
        let quizId;
        try {
            const res = await fetch("/quizzes-api/manage/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify(quizData),
            });
            if (!res.ok) {
                const err = await res.json();
                msg.textContent = "Failed to create quiz: " + JSON.stringify(err);
                return;
            }
            const created = await res.json();
            quizId = created.id;
        } catch (e) {
            msg.textContent = "Error creating quiz.";
            return;
        }

        // Step 2: add each question with its answers
        for (const block of questionBlocks) {
            const questionText = block.querySelector(".question-text").value.trim();
            const answerRows = block.querySelectorAll(".answer-row");
            const answers = [];

            for (const row of answerRows) {
                const text = row.querySelector(".answer-text").value.trim();
                const isCorrect = row.querySelector(".answer-correct").checked;
                if (text) {
                    answers.push({ answer_text: text, is_correct: isCorrect });
                }
            }

            if (answers.length < 2) {
                msg.textContent = `Question "${questionText}" needs at least 2 answers.`;
                return;
            }

            try {
                const res = await fetch(`/quizzes-api/manage/${quizId}/questions/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCSRFToken(),
                    },
                    body: JSON.stringify({ question_text: questionText, answers: answers }),
                });
                if (!res.ok) {
                    const err = await res.json();
                    msg.textContent = `Failed to save question "${questionText}": ` + JSON.stringify(err);
                    return;
                }
            } catch (e) {
                msg.textContent = `Error saving question "${questionText}".`;
                return;
            }
        }

        msg.textContent = "Quiz created successfully!";
        document.getElementById("create-quiz-form").reset();
        document.getElementById("questions-container").innerHTML = "";
        questionCount = 0;
    }
});

function getCSRFToken() {
    return document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="))
        ?.split("=")[1];
}
