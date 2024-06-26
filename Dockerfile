FROM ghcr.io/binkhq/python:3.11-pipenv

WORKDIR /app
ADD . .

RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "gunicorn", "--error-logfile=-", "--access-logfile=-", "--bind=0.0.0.0:9000", "wsgi:application" ]
