FROM python:3.6-slim

RUN apt update && apt install -y gcc make

RUN python -m pip install --upgrade pip

COPY ./coach_requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/coach_requirements.txt
RUN python -c "import nltk; nltk.download('stopwords');"