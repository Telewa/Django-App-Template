FROM python:3.9.17-bullseye

RUN apt update

# Install additional tools needed for build & run
RUN apt-get install -y vim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /my_app
ADD . .

ARG PIP_CONFIG_FILE
ENV PIP_CONFIG_FILE=${PIP_CONFIG_FILE}
RUN pip install -U pip
RUN pip install -r requirements.txt
