FROM python:3.12-bullseye
EXPOSE 80
VOLUME /data/
VOLUME /static/
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install -y \
                    supervisor \
                    dumb-init


CMD rm -rf static; ln -s /static static; \
    python ./manage.py migrate; \
    python ./manage.py collectstatic --noinput; \
    /usr/bin/supervisord

COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisor/ /etc/supervisor/conf.d/

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code

