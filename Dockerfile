FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt

RUN  pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "doroshenkoaldm/manage.py",  "runserver", "8000:8000"]