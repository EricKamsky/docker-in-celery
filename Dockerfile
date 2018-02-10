FROM python:3.6-alpine

RUN apk add --update --no-cache docker

RUN pip install pipenv --upgrade --no-cache-dir

WORKDIR /app

COPY Pipfile .
RUN pipenv install --system

VOLUME [ "/app/tasks.py" ]

CMD [ "celery", "-A", "tasks", "worker", "-c", "1" ]
