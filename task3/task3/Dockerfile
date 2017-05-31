FROM python:3.4

RUN mkdir /task3

ADD . /task3

WORKDIR /task3

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
