from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

QUESTIONS = [
    {
        "id": 1,
        "question": "Which language is used with Flask?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "id": 2,
        "question": "HTML stands for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Tool Markup Language",
            "Home Text Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "id": 3,
        "question": "CSS is used for?",
        "options": [
            "Programming",
            "Styling",
            "Database",
            "Networking"
        ],
        "answer": "Styling"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/questions")
def questions():
    data = []

    for q in QUESTIONS:
        data.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"]
        })

    return jsonify(data)


@app.route("/submit", methods=["POST"])
def submit():
    answers = request.json

    score = 0

    for q in QUESTIONS:
        if answers.get(str(q["id"])) == q["answer"]:
            score += 1

    return jsonify({
        "score": score,
        "total": len(QUESTIONS)
    })


if __name__ == "__main__":
    app.run(debug=True)