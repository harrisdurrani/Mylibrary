ARG PYTHON_IMAGE=python:3.8-buster

FROM ${PYTHON_IMAGE} as library_site

RUN apt-get update && apt-get install -y --no-install-recommends gettext

RUN pip install pipenv

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN pipenv install --deploy --ignore-pipfile

WORKDIR /code/library

ENTRYPOINT [ "bash" ]