from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Quiz questions stored in Python
quiz_data = {
    "easy": [
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
        {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": "8"},
        {"question": "What is 10 - 5?", "options": ["2", "3", "5", "7"], "answer": "5"},
        {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "Tokyo"},
        {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "NaCl"], "answer": "H2O"},
        {"question": "What is the currency of the USA?", "options": ["Euro", "Dollar", "Pound", "Yen"], "answer": "Dollar"},
        {"question": "What is 8 / 2?", "options": ["2", "3", "4", "5"], "answer": "4"}
    ],
    "medium": [
        {"question": "What is 5 * 5?", "options": ["20", "25", "30", "35"], "answer": "25"},
        {"question": "What is the largest planet in the solar system?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"},
        {"question": "What is the capital of Germany?", "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"], "answer": "Berlin"},
        {"question": "What is the boiling point of water in Celsius?", "options": ["90", "100", "110", "120"], "answer": "100"},
        {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "answer": "Leonardo da Vinci"}
    ],
    "hard": [
        {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"], "answer": "Harper Lee"},
        {"question": "What is 12 * 12?", "options": ["144", "121", "132", "156"], "answer": "144"},
        {"question": "What is the capital of Russia?", "options": ["Moscow", "St. Petersburg", "Kazan", "Sochi"], "answer": "Moscow"},
        {"question": "What is 18 / 3?", "options": ["5", "6", "7", "8"], "answer": "6"}
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz/<difficulty>", methods=["GET", "POST"])
def quiz(difficulty):
    questions = quiz_data.get(difficulty, [])

    if request.method == "POST":
        score = 0
        results = []
        for i, question in enumerate(questions):
            user_answer = request.form.get(f"q{i}", "")
            correct_answer = question["answer"]
            if user_answer == correct_answer:
                score += 1
            results.append((question["question"], user_answer, correct_answer))
        
        return render_template("result.html", score=score, total=len(questions), results=results)

    return render_template("quiz.html", difficulty=difficulty, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
