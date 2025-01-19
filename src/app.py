from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# In-memory storage for quizzes (for simplicity)
quizzes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    title = request.form['title']
    skill = request.form['skill']
    level = request.form['level']
    content = request.form['content']

    if skill not in quizzes:
        quizzes[skill] = {}
    if level not in quizzes[skill]:
        quizzes[skill][level] = []

    try:
        quiz_data = {
            "title": title,
            "content": content
        }
        quizzes[skill][level].append(quiz_data)
        return jsonify({"message": "Quiz successfully added!"}), 200
    except Exception as e:
        return jsonify({"message": "Failed to add quiz", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
