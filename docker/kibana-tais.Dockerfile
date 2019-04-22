from python:3.6

env PYTHONUNBUFFERED 1

run mkdir /kibana-tais
workdir /kibana-tais

add ./kibana-tais/requirements.txt /kibana-tais/

run pip install -r requirements.txt

add ./kibana-tais /kibana-tais/

env PORT=8081                             \
    ALLOWED_HOSTS=localhost               \
    PREFIX_URL=

cmd python manage.py runserver 0.0.0.0:$PORT
