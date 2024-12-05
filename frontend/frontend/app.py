from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit1', methods=['POST'])
def submit1():
    data = request.form.get('data')
    # Отправляем POST запрос на Java backend
    response = requests.post('http://localhost:8080/submit1', data=data)
    return render_template('index.html', result=response.text)

@app.route('/submit2', methods=['GET'])
def submit2():
    try:
        response = requests.get('http://localhost:8080/submit2')
        return render_template('index.html', file_content=response.text)
    except requests.exceptions.RequestException as e:
        return render_template('index.html', file_content="Ошибка соединения с backend")

if __name__ == '__main__':
    app.run(debug=True)

