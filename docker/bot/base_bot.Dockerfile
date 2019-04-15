FROM python:3.6-slim

RUN apt update && apt install -y gcc make curl

RUN python -m pip install --upgrade pip

COPY ./bot_requirements.txt /tmp

RUN pip install -r /tmp/bot_requirements.txt
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
