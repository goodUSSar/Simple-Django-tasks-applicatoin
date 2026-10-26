# Небольшой Django-проект «Мои задачи»

Простой учебный проект без DevOps-настроек.

## Что используется

- Django
- SQLite
- Django Templates
- HTML и CSS

В проекте нет Docker, Kubernetes, Nginx, Gunicorn, systemd, API и переменных окружения.

## Возможности

- добавить задачу;
- отметить задачу выполненной;
- вернуть задачу в активное состояние;
- удалить задачу;
- посмотреть задачи через Django Admin.

## Запуск на Linux

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip unzip

unzip simple_django_tasks.zip
cd simple_django_tasks

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Открыть в браузере:

```text
http://127.0.0.1:8000
```

Остановить сервер: `Ctrl+C`.

## Админ-панель

Создать администратора:

```bash
python manage.py createsuperuser
```

Открыть:

```text
http://127.0.0.1:8000/admin/
```

## Повторный запуск

```bash
cd simple_django_tasks
source .venv/bin/activate
python manage.py runserver
```

Выход из виртуального окружения:

```bash
deactivate
```
