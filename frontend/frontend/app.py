from flask import Flask, request, render_template
import requests  # для отправки запросов на Java backend

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Форма для отправки данных (submit1)
@app.route('/submit1', methods=['POST'])
def submit1():
    data = request.form.get('data')
    # Отправляем POST запрос на Java backend
    response = requests.post('http://backend:8080/submit1', data=data)
    return render_template('index.html', result=response.text)


# Форма для запроса данных из файла (submit2)
@app.route('/submit2', methods=['GET'])
def submit2():
    try:
        # Запрашиваем данные с Java backend
        response = requests.get('http://backend:8080/submit2')
        return render_template('index.html', file_content=response.text)
    except requests.exceptions.RequestException as e:
        return render_template('index.html', file_content="Ошибка соединения с backend")

if __name__ == '__main__':
    app.run(debug=True)


