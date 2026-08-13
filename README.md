# rental-ops-django

## Description
A study project

## How to install
To install Python and Django versions for the project, run:
```
uv sync
```

To check installed version, use:
```
uv run python --version
uv run django-admin --version
```

## What's inside

- `config/` folder contains most of the project configuration. The following files descibes what exacly is inside it.
- `manage.py` is a Django's API to the project. It allows to add apps, make and run migrations, run dev server and many more.
- `settings.py` contains all the settings for the project, including DB setup, apps, templates, middlewares and so on.
- `urls.py` is like a router for the app
- `wsgi.py` and `asgi.py` are "servers", the second one is async
