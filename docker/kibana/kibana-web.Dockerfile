from python:3.6

env PYTHONUNBUFFERED 1

run mkdir /kibana-web
workdir /kibana-web

add ./kibana-web/requirements.txt /kibana-web/

run pip install -r requirements.txt

add ./kibana-web /kibana-web/

env PORT=8080                             \
    ALLOWED_HOSTS=localhost               \
    PREFIX_URL=

cmd python manage.py runserver 0.0.0.0:$PORT
