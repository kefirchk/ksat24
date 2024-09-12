# Инструкция по развертыванию

---

## Описание

---

Это руководство объясняет, как развернуть веб-приложение Flask, использующее SQLAlchemy и PostgreSQL, с помощью Docker и Docker Compose.

## Структура проекта

---

```plaintext
ksat24/
│
├── app/
│   ├── __init__.py           # Файл для создания экземплера приложения
│   ├── main.py               # Основной файл приложения Flask
│   ├── config.py             # Файл конфигурации
│   ├── views.py              # Описание конечных точек
│   ├── database/
│   │   ├── __init__.py      
│   │   └── database.py       # Файл с моделями для БД и экземпляром БД
│   │
│   ├── repositories/
│   │   ├── __init__.py 
│   │   └── repository.py     # Файл для работы с БД
│   │
│   ├── services/
│   │   ├── __init__.py 
│   │   └── input_service     # Сервис работы с инпутами
│   │
│   ├── static/
│   │   ├── index.html        # Главное окно с инпутами
│   │   └── results.html      # Для просмотра инпутов
│   │ 
│   └── templates/
│       ├── main.js           # Логика инпутов
│       └── styles.js          # Общие стили
│         
├── docker-compose.yml        # Конфигурация Docker Compose
├── Dockerfile                # Dockerfile для сборки образа приложения
├── .env                      # Файл с переменными окружения
├── requirements.txt          # Список зависимостей Python
└── README.md                 # Этот файл
```

## Требования

---

- Docker
- Docker Compose
- Linux

## Шаги по развертыванию

---

### 1. Клонируйте репозиторий

Клонируйте репозиторий с кодом на вашу локальную машину:

```bash
git clone https://github.com/kefirchk/ksat24.git
cd ksat24
```

### 2. Настройте переменные окружения

Создайте файл ***.env*** в корне проекта и заполните следующие переменные вашими значениями:

```plaintext
# .env

POSTGRES_USER=postgres          # имя пользователя
POSTGRES_PASSWORD=1234          # пароль к БД
POSTGRES_DB=flaskdb             # название БД
POSTGRES_PORT=5432              # порт, на котором работает БД
POSTGRES_HOST=db                # адрес БД
```

### 3. Соберите и запустите контейнеры

Используйте команду Docker Compose для сборки и запуска контейнеров:

```bash
docker-compose up --build
```

### 4. Доступ к приложению

После успешного запуска приложение будет доступно по адресу http://localhost:5000.

### 5. Завершение работы

Чтобы остановить и удалить контейнеры, выполните:

```bash
docker-compose down
```
