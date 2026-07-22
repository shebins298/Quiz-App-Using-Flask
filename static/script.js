let questions = [];

async function loadQuestions() {
  const response = await fetch("/questions");
  questions = await response.json();

  const form = document.getElementById("quizForm");

  questions.forEach((q) => {
    const div = document.createElement("div");
    div.className = "question";

    let html = `<h3>${q.question}</h3>`;

    q.options.forEach((option) => {
      html += `
            <label>
                <input type="radio"
                name="${q.id}"
                value="${option}">
                ${option}
            </label><br>
            `;
    });

    div.innerHTML = html;

    form.appendChild(div);
  });
}

async function submitQuiz() {
  let answers = {};

  questions.forEach((q) => {
    const selected = document.querySelector(`input[name="${q.id}"]:checked`);

    if (selected) {
      answers[q.id] = selected.value;
    }
  });

  const response = await fetch("/submit", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(answers),
  });

  const result = await response.json();

  document.getElementById(
    "result"
  ).innerHTML = `Score: ${result.score} / ${result.total}`;
}

loadQuestions();
