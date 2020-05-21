FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir colorama libsast && \
    pip install -e /usr/src/app/njsscan

ENTRYPOINT ["njsscan"]