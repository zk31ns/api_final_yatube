# Yatube API 🚀

REST API для социальной сети Yatube, позволяющее работать с постами, комментариями и подписками через API-интерфейс.

## 📖 Описание

Данный проект предоставляет полнофункциональный REST API для платформы Yatube. API позволяет создавать, редактировать, удалять и просматривать посты, комментарии, а также управлять подписками на других пользователей.

### 🔑 Ключевые возможности:
- ✅ Создание и управление постами
- ✅ Комментирование постов
- ✅ Система подписок на пользователей
- ✅ Аутентификация по токенам
- ✅ Фильтрация и поиск
- ✅ Пагинация результатов

## 👨‍💻 Автор

**Давыдов Александр Васильевич**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/zk31ns/api_final_yatube)

## 🛠 Технологический стек

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Django](https://img.shields.io/badge/Django-3.2-green?logo=django)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.12-red?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-3.x-lightgrey?logo=sqlite)

- **Python 3.9** - основной язык программирования
- **Django 3.2** - веб-фреймворк
- **Django REST Framework** - создание API
- **Django Filter** - фильтрация данных
- **SQLite** - база данных

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone git@github.com:zk31ns/api_final_yatube.git
cd api_final_yatube
```

### 2. Создание виртуального окружения
```bash
python3 -m venv venv

# Активация:
# Linux/MacOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Установка зависимостей
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Миграции базы данных
```bash
python manage.py migrate
```

### 5. Запуск сервера
```bash
python manage.py runserver
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000/`

## 📚 Примеры API-запросов

### 🔐 Аутентификация
```python
import requests

headers = {
    "Authorization": "Token ваш_токен_авторизации",
    "Content-Type": "application/json"
}
```

### 📝 Работа с постами

**Получение списка постов:**
```python
import requests

url = "http://127.0.0.1:8000/api/v1/posts/"
response = requests.get(url)

print(f"Status: {response.status_code}")  # 200
print(response.json())  # JSON с постами
```

**Создание нового поста:**
```python
data = {
    "text": "Текст нового поста",
    "group": 1  # опционально
}
response = requests.post(url, json=data, headers=headers)

print(f"Status: {response.status_code}")  # 201
```

### 💬 Комментарии

**Добавление комментария:**
```python
post_id = 1
url = f"http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/"

data = {"text": "Отличный пост!"}
response = requests.post(url, json=data, headers=headers)
```

### 👥 Подписки

**Подписка на пользователя:**
```python
url = "http://127.0.0.1:8000/api/v1/follow/"

data = {"following": "username"}
response = requests.post(url, json=data, headers=headers)
```

## 📁 Структура API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/api/v1/posts/` | Список постов |
| POST | `/api/v1/posts/` | Создание поста |
| GET | `/api/v1/posts/{id}/` | Детали поста |
| PUT/PATCH | `/api/v1/posts/{id}/` | Обновление поста |
| DELETE | `/api/v1/posts/{id}/` | Удаление поста |
| GET | `/api/v1/posts/{id}/comments/` | Комментарии поста |
| POST | `/api/v1/posts/{id}/comments/` | Добавить комментарий |
| GET | `/api/v1/follow/` | Мои подписки |
| POST | `/api/v1/follow/` | Подписаться |

## 🔒 Безопасность

- Аутентификация по токенам
- Авторизация на основе прав доступа
- Защита от CSRF-атак
- Валидация входных данных

---

⭐ Не забудьте поставить звезду репозиторию, если проект был полезен!
