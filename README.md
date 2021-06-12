**Activating Virtual Environment**

```pip install virtualenv```

```virtualenv venv```


**Activate virtual environment**

```venv/scripts/activate```


**Installing Dependencies**

```pip install requirements.txt```


**Starting Django Project**

```django-admin startproject tasker .```


**Starting Django App**

```python manage.py startapp tasks```


**Configuring env file**

```
EMAIL_HOST = smtp.gmail.com
EMAIL_HOST_USER = Your Mail Id
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = Your Mail Id
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = Your Mail Password

SECRET_KEY = 'Djago app secret key (get this from settings.py)'
DEBUG = True

#DataBase credentials
export NAME = database name
export USER = postgres
export PASSWORD = database password
export HOST = localhost
```
