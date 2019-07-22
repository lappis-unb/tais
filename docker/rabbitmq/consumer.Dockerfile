FROM python:3.6-slim

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -I pika==1.1.0 elasticsearch==6.3.1
