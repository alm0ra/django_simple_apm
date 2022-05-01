FROM python:3.9
LABEL MAINTAINER="Ali Moradi | ali.mrd318@gmail.com"
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y git curl gnupg binutils libproj-dev gdal-bin gettext postgresql-client supervisor

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -U gunicorn


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get remove git -y; apt-get autoremove -y; apt-get clean
ENV C_FORCE_ROOT=1

COPY . /code
RUN rm -rf .git
WORKDIR /code

RUN mkdir logs
ENV NEW_RELIC_CONFIG_FILE=/code/newrelic.ini \
    NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
    
RUN export NEW_RELIC_CONFIG_FILE

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
