FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc musl-dev \
  && apk add postgresql-dev \
  && apk add git\
  && apk add make

RUN pip install --upgrade pip
COPY ./requirements /requirements
RUN pip install -r /requirements/base.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
