FROM python:3.8 as build-python

WORKDIR /app

RUN apt-get -y update \
    && apt-get -y install \
    gettext \
    libxml2 \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# ---------------------------------------------------------------------------- #
# PACKAGE
# ---------------------------------------------------------------------------- #
FROM python:3.8-slim

WORKDIR /app

RUN apt-get -y update \
    && apt-get install -y \
    gettext \
    libxml2 \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY lexmax /app/

RUN mkdir -p /app/public/media /app/public/static \
    && groupadd -r andres -g 1000 \
    && useradd -r -u 1000 -g andres andres \
    && chown -R andres:andres /app

USER andres

ENV PYTHONUNBUFFERED 1
ENV PROCESSES 1

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "application.asgi:application", "--access-log", "-", "--verbosity", "3"]
