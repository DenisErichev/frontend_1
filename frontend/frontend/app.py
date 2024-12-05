from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']

    response = requests.post('http://localhost:8080/api/data', data={'text': text})
    return f"Ответ бэкенда: {response.text}"


if __name__ == '__main__':
    app.run(debug=True)
