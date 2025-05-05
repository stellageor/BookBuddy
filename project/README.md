# Django BookBuddy Project

This is a Django-based platform called **BookBuddy**, which allows users to borrow or exchange books. The project includes features such as user authentication, book management, and profile settings.

## Features

- User registration and login.
- View and manage books.
- Add, edit, and delete books.
- Manage account and profile settings.
- Access the admin interface for managing users and content.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package manager)
- virtualenv (recommended for creating isolated environments)

## Installation

1. Create & activate a virtualenv

```
pip install virtualenv            # if you don’t have it
virtualenv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

1. Install dependencies

```
pip install -r requirements.txt
```

1. Database migrations

```
python manage.py makemigrations
python manage.py migrate
```

## Run the development server

```
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Log in with `admin` / `admin`

## Folder Structure

```
bookbuddy/
├── core/
│   ├── migrations/
│   ├── templates/core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── ...
├── bookbuddy/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
├── templates/
├── requirements.txt
└── manage.py
```
