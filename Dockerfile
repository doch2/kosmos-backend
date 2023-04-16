FROM python:3.9


EXPOSE 80


RUN mkdir /app
COPY . /app
WORKDIR /app

RUN chown -R 1000:1000 /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "server.py"]