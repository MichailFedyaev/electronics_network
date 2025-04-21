# Сеть по продаже электроники

Веб-приложение с API-интерфейсом и админ-панелью для управления сетью поставщиков электроники.

## Описание

Проект представляет собой систему управления сетью поставщиков электроники с иерархической структурой из трех уровней:
- Завод (уровень 0)
- Розничная сеть (уровень 1)
- Индивидуальный предприниматель (уровень 2)

Каждое звено сети может ссылаться на любого поставщика в системе, при этом уровень иерархии определяется отношением к другим элементам сети.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/MichailFedyaev/electronics_network
cd electronics_network
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения:
Создайте файл `.env` в корне проекта со следующими переменными:
```
SECRET_KEY=your-secret-key
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=your-db-port
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя:
```bash
python manage.py csu
```

7. Загрузите тестовые данные:
```bash
python manage.py add_test_data
```

8. Запустите сервер:
```bash
python manage.py runserver
```

## Кастомные команды

### Создание суперпользователя
```bash
python manage.py csu [--username USERNAME] [--email EMAIL] [--password PASSWORD]
```
По умолчанию создает пользователя:
- username: admin
- email: admin@example.com
- password: 123qwe456rty

### Загрузка тестовых данных
```bash
python manage.py add_test_data
```
Создает тестовых поставщиков и продукты для демонстрации функционала.

## API Документация

После запуска сервера документация доступна по адресам:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## API Endpoints

### Поставщики

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/api/suppliers/` | Список поставщиков (фильтр по стране: `?country=Россия`) |
| POST | `/api/suppliers/` | Создание поставщика |
| PUT/PATCH | `/api/suppliers/<id>/` | Обновление (поле debt — только для чтения) |
| DELETE | `/api/suppliers/<id>/` | Удаление поставщика |

### Аутентификация (JWT)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | `/api/users/token/` | Получить access и refresh токены |
| POST | `/api/users/token/refresh/` | Обновить access токен |
| POST | `/api/users/token/verify/` | Проверка токена на валидность |

## Админ-панель

Доступна по адресу: http://localhost:8000/admin/

Функционал:
- Просмотр и управление поставщиками и продуктами
- Фильтрация по городу
- Очистка задолженности у выбранных поставщиков
- Просмотр иерархии поставщиков

## Технические детали

- Django 5.2
- Django REST Framework
- Simple JWT для аутентификации
- PostgreSQL
- Loguru для логирования
- Swagger/ReDoc для документации API

## Права доступа

- API доступен только для активных сотрудников
- Админ-панель доступна только для суперпользователей
- Поле задолженности (debt) доступно только для чтения через API
