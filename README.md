# api_final
Данный api предоставляет следующие возможности пользователям: создание постов, комментариев, их редактирование, удаление и возможность подписываться на пользователей. api имеет простой и понятный интерфейс, который вы сможете легко интегрировать в вашу систему. К тому же, данное api обеспечивает безопасность данных с помощью проверки подлинности и авторизации. Можете быть уверены, что ваши данные будут защищены.

## Примеры API-запросов к Django REST Framework (DRF)
GET-запрос (получение списка объектов)

import requests

url = "http://127.0.0.1:8000/api/books/"  # Пример API для книг
response = requests.get(url)

print(response.status_code)  # 200 (OK)
print(response.json())  # Вывод JSON-ответа
С фильтрацией (?author=Толстой):

params = {"author": "Толстой"}
response = requests.get(url, params=params)

POST-запрос (создание объекта)

import requests

url = "http://127.0.0.1:8000/api/books/"
data = {
    "title": "Война и мир",
    "author": "Толстой",
    "year": 1869
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)  # 201 (Created)
print(response.json())  # {"id": 1, "title": "Война и мир", ...}
Если API требует токен аутентификации:

headers = {
    "Authorization": "Token ваш_токен",  # Или "Bearer ваш_jwt_токен"
    "Content-Type": "application/json"
}
response = requests.post(url, json=data, headers=headers)
PUT/PATCH-запрос (обновление объекта)

import requests

book_id = 1
url = f"http://127.0.0.1:8000/api/books/{book_id}/"
data = {"year": 1870}  # Изменяем год

PUT (полное обновление) или PATCH (частичное)
response = requests.patch(url, json=data)
print(response.status_code)  # 200 (OK)
DELETE-запрос (удаление объекта)

import requests

book_id = 1
url = f"http://127.0.0.1:8000/api/books/{book_id}/"

response = requests.delete(url)
print(response.status_code)

## Автор
Давыдов Александр Васильевич
Github:
https://github.com/zk31ns/api_final_yatube


## Как запустить проект:

### 1. Клонирование
git clone git@github.com:zk31ns/api_final_yatube.git
\
cd api_final_yatube

### 2. Настройка окружения

python -m venv venv
\
source venv/bin/activate  (Linux/MacOs)
\
venv\Scripts\activate  (Windows)

### 3. Установка зависимостей
pip install -r requirements.txt
python -m pip install --upgrade pip

### 4. Применение миграций
python manage.py migrate

### 5. Запуск сервера
python manage.py runserver
