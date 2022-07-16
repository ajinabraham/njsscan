FROM python:3.9-slim-buster

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

COPY . /usr/src/njsscan

WORKDIR /usr/src/njsscan

RUN pip install -e .

ENTRYPOINT ["njsscan"]