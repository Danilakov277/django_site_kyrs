# 🛍️ Django Shop Project

Современный веб-сайт магазина, построенный на Django с системой пользователей, отзывов, статей и корзины покупок.

## 🚀 Быстрый старт

### Для новых пользователей
Если вы впервые настраиваете проект, выполните следующие шаги:

1. **Установите PostgreSQL** (если не установлен)
2. **Создайте базу данных и пользователя** (см. раздел "Настройка PostgreSQL")
3. **Обновите настройки** в `shop/settings.py`
4. **Установите зависимости** и запустите проект

### Предварительные требования
- PostgreSQL должен быть установлен и запущен
- Создайте базу данных для проекта
- Настройте пользователя PostgreSQL

## 🗄️ Настройка PostgreSQL

### 1. Установка PostgreSQL
Скачайте и установите PostgreSQL с официального сайта: https://www.postgresql.org/download/

### 2. Создание базы данных и пользователя

#### Windows (через psql):
```sql
-- Подключитесь к PostgreSQL как суперпользователь
psql -U postgres

-- Создайте базу данных
CREATE DATABASE django_shop_db;

-- Создайте пользователя
CREATE USER your_username WITH PASSWORD 'your_password';

-- Дайте права пользователю
GRANT ALL PRIVILEGES ON DATABASE django_shop_db TO your_username;

-- Выйдите
\q
```

#### Linux/macOS:
```bash
# Создание базы данных
sudo -u postgres createdb django_shop_db

# Создание пользователя
sudo -u postgres createuser --interactive your_username

# Установка пароля
sudo -u postgres psql -c "ALTER USER your_username PASSWORD 'your_password';"

# Дать права
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE django_shop_db TO your_username;"
```

### 3. Настройка Django
Обновите настройки в `shop/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_shop_db',        # Ваша база данных
        'USER': 'your_username',         # Ваш пользователь
        'PASSWORD': 'your_password',      # Ваш пароль
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Пример полной настройки

#### Вариант 1: Использование стандартной базы данных `postgres`
```sql
-- 1. Подключитесь к PostgreSQL как суперпользователь
psql -U postgres

-- 2. Создайте пользователя (если нужно)
CREATE USER myuser WITH PASSWORD 'mypassword';

-- 3. Дайте права на базу данных postgres
GRANT ALL PRIVILEGES ON DATABASE postgres TO myuser;

-- 4. Выйдите
\q
```

#### Вариант 2: Создание отдельной базы данных
```sql
-- 1. Подключитесь к PostgreSQL
psql -U postgres

-- 2. Создайте базу данных
CREATE DATABASE django_shop_db;

-- 3. Создайте пользователя
CREATE USER myuser WITH PASSWORD 'mypassword';

-- 4. Дайте права
GRANT ALL PRIVILEGES ON DATABASE django_shop_db TO myuser;

-- 5. Выйдите
\q
```

#### Настройка в .env файле:
```env
# Для варианта 1 (стандартная база postgres)
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_password

# Для варианта 2 (отдельная база)
DB_NAME=django_shop_db
DB_USER=myuser
DB_PASSWORD=mypassword
```

### Windows

#### 1. Клонирование и настройка
```powershell
# Перейдите в директорию проекта
cd C:\Users\Anzherus\Desktop\django_site_kyrs

# Активируйте виртуальное окружение
.\venv\Scripts\Activate.ps1

# Установите зависимости (если не установлены)
pip install -r requirements.txt
```

#### 2. Настройка базы данных
```powershell
# Выполните миграции
python manage.py migrate

# Создайте суперпользователя (опционально)
python manage.py createsuperuser
```

#### 3. Запуск сервера
```powershell
# Запустите сервер разработки
python manage.py runserver
```

#### 4. Открытие в браузере
Откройте браузер и перейдите по адресу: **http://127.0.0.1:8000**

---

### Linux/macOS

#### 1. Клонирование и настройка
```bash
# Перейдите в директорию проекта
cd /path/to/django_site_kyrs

# Активируйте виртуальное окружение
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
```

#### 2. Настройка базы данных
```bash
# Выполните миграции
python manage.py migrate

# Создайте суперпользователя (опционально)
python manage.py createsuperuser
```

#### 3. Запуск сервера
```bash
# Запустите сервер разработки
python manage.py runserver

# Или используйте готовый скрипт
./run_django.sh
```

#### 4. Открытие в браузере
Откройте браузер и перейдите по адресу: **http://127.0.0.1:8000**

---

## 📋 Требования

### Системные требования
- Python 3.8+
- pip
- Виртуальное окружение (venv)
- PostgreSQL (база данных)

### Зависимости проекта
```
Django==5.2.6
pillow==11.3.0
psycopg2-binary==2.9.10    # PostgreSQL драйвер
python-dotenv==1.1.1
whitenoise==6.11.0
gunicorn==23.0.0
```

**База данных:** PostgreSQL (не SQLite)

---

## 🗂️ Структура проекта

```
django_site_kyrs/
├── 📁 articles/          # Модуль статей
├── 📁 cart/             # Модуль корзины
├── 📁 main/             # Основной модуль (товары/услуги)
├── 📁 review/           # Модуль отзывов
├── 📁 user/             # Модуль пользователей
├── 📁 shop/             # Настройки Django
├── 📁 static/           # Статические файлы (CSS, JS)
├── 📁 templates/        # HTML шаблоны
├── 📄 manage.py         # Django управление
├── 📄 requirements.txt  # Зависимости
└── 📄 README.md         # Документация
```

---

## ⚙️ Настройка

### Переменные окружения
Создайте файл `.env` в корне проекта на основе `env.example`:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Settings
DB_NAME=django_shop_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Настройки базы данных
Проект использует переменные окружения для настройки PostgreSQL. Настройки в `shop/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'django_shop_db'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

**Настройка через .env файл:**
1. Скопируйте `env.example` в `.env`
2. Заполните ваши данные базы данных
3. Перезапустите Django

**Требования для работы:**
- PostgreSQL должен быть установлен и запущен
- База данных должна быть создана (см. раздел "Настройка PostgreSQL")
- Пользователь PostgreSQL должен иметь права доступа к базе данных

---

## 🎯 Основные функции

### 👤 Система пользователей
- Регистрация и авторизация
- Профили пользователей
- Система достижений и прогресса
- Уведомления

### 🛒 Магазин
- Каталог товаров и услуг
- Корзина покупок
- Детальные страницы товаров

### 📝 Контент
- Система статей
- Отзывы пользователей
- Административная панель

### 🎨 Дизайн
- Адаптивный дизайн
- Современный UI/UX
- Темная/светлая тема

---

## 🛠️ Команды разработки

### Основные команды Django
```bash
# Запуск сервера
python manage.py runserver

# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Сбор статических файлов
python manage.py collectstatic
```

### Управление данными
```bash
# Загрузка категорий прогресса
python manage.py load_progress_categories

# Загрузка достижений
python manage.py load_achievements
```

### Полезные скрипты
```bash
# Проверка подключения к базе данных
python check_db.py

# Автоматическая настройка базы данных
python setup_db.py
```

---

## 🚀 Развертывание

### Локальная разработка
```bash
# Windows
.\venv\Scripts\Activate.ps1
python manage.py runserver

# Linux/macOS
source venv/bin/activate
python manage.py runserver
```

### Продакшн
```bash
# Сбор статических файлов
python manage.py collectstatic

# Запуск с Gunicorn
gunicorn shop.wsgi:application
```

---

## 🐛 Решение проблем

### Ошибка "ModuleNotFoundError: No module named 'psycopg2'"
```bash
# Установите psycopg2 для PostgreSQL
pip install psycopg2-binary
```

### Ошибка подключения к PostgreSQL
1. **Убедитесь, что PostgreSQL запущен:**
   ```bash
   # Windows
   netstat -an | findstr :5432
   
   # Linux/macOS
   sudo systemctl status postgresql
   ```

2. **Проверьте настройки в `shop/settings.py`** - используйте переменные окружения

3. **Проверьте, что база данных существует:**
   ```sql
   -- Подключитесь к PostgreSQL
   psql -U postgres
   
   -- Проверьте список баз данных
   \l
   
   -- Если базы нет, создайте её
   CREATE DATABASE your_database_name;
   ```

4. **Проверьте права пользователя:**
   ```sql
   -- Дайте права пользователю
   GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user;
   ```

5. **Убедитесь, что пароль правильный** - проверьте в .env файле

### Проблемы с миграциями
```bash
# Применение миграций к PostgreSQL
python manage.py migrate

# Сброс миграций (ОСТОРОЖНО!)
python manage.py migrate --fake-initial
```

### Проверка подключения к PostgreSQL
```bash
# Проверка статуса Django
python manage.py check

# Проверка миграций
python manage.py showmigrations

# Тест подключения к базе данных
python manage.py dbshell

# Специальный скрипт проверки (рекомендуется)
python check_db.py
```

### Проверка настроек
Убедитесь, что в `shop/settings.py` правильно указаны:
- `NAME` - имя вашей базы данных
- `USER` - ваш пользователь PostgreSQL  
- `PASSWORD` - пароль пользователя
- `HOST` - обычно 'localhost'
- `PORT` - обычно '5432'

---

## 📞 Поддержка

Если у вас возникли проблемы:

1. Проверьте, что все зависимости установлены
2. Убедитесь, что виртуальное окружение активировано
3. Убедитесь, что PostgreSQL запущен и доступен
4. Проверьте настройки базы данных в `shop/settings.py`
5. Выполните миграции: `python manage.py migrate`
6. Проверьте подключение: `python manage.py check`

---

## 📄 Лицензия

Этот проект создан в образовательных целях.

---

**🎉 Готово! Ваш Django проект запущен и готов к работе!)))**
