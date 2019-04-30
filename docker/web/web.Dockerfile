FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /web
WORKDIR /web

COPY ./web/requirements.txt /web/

RUN pip install -r requirements.txt

COPY ./web /web/

ENV PORT=8000                             \
    ROCKETCHAT_URL=http://localhost:3000  \
    ALLOWED_HOSTS=localhost               \
    PREFIX_URL=

CMD python manage.py runserver 0.0.0.0:$PORT
