# Используем минимальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости без кэширования, чтобы минимизировать размер образа
RUN pip install --no-cache-dir flask requests

# Устанавливаем переменную среды для Flask
ENV FLASK_APP=app.py

# Запускаем Flask
CMD ["flask", "run", "--host=0.0.0.0"]