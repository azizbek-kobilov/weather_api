# weather-api
API and telegram bot for receiving weather data

### Setup

Clone the repository:
```sh
$ git clone https://github.com/azizbek-kobilov/weather_api.git
$ cd weather-api
```

Create a virtual environment:
```sh
$ python -m venv env
$ source env/bin/activate
```

Install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```

In the root of the project create a .env file and set the environment variables
```sh
# Django Secret Key
SECRET_KEY = 

# Telegram token
BOT_TOKEN = 

# Weather API Key
YANDEX_KEY = 
```

Migrate database:
```sh
(env)$ python manage.py migrate
```

Create superuser:
```sh
(env)$ python manage.py createsuperuser
```

Run project:
```sh
(env)$ python manage.py runserver
```

Run telegram bot:
```sh
(env)$ python manage.py runbot
```
