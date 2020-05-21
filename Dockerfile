FROM python:3-alpine

RUN pip install --no-cache-dir njsscan

ENTRYPOINT ["njsscan"]