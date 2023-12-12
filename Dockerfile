FROM python:3.10.11-slim-buster

RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","main.py"]
