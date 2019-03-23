# home inventory tracking

## How to run with Docker
* cd into project's root folder
* hit "docker-compose up"
* wait a little bit, don't worry it might output some errors about database connections when booting up
* Browse http://127.0.0.1:5500

## How to run on local environment
* Make sure postgresql installed
* Create "metglobal_hit" database
* cd into project's root folder
* hit "pip install -r requirements.txt"
* hit "python manage.py migrate"
* hit "python manage.py runserver"
* Browse http://127.0.0.1:8000

_Note that this project is not production grade, we are using django's development server to test it out_
