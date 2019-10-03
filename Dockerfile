FROM python:3.6.4-alpine3.7

ENV LANG C.UTF-8

RUN apk update && \
    apk upgrade && \
    pip install --no-cache-dir requests

COPY script/github-buildstatus-notifier.py /github-buildstatus-notifier.py

ENTRYPOINT ["python", "/github-buildstatus-notifier.py"]