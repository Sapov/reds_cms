FROM ubuntu:latest
LABEL authors="sasha"

FROM python:3.10.4

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash django && chmod 777 /opt /run

WORKDIR /django
RUN mkdir /django/media
RUN mkdir /django/media/image
RUN mkdir /django/static
RUN mkdir /django/media/orders  && mkdir /django/media/arhive && chown -R django:django /django && chmod 755 /django

COPY --chown=django:django . .
#COPY . /django

RUN pip install -r requirements.txt

USER django

CMD ["gunicorn","-b","0.0.0.0:8000","mysite.wsgi:application"]