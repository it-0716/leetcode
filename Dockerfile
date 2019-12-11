FROM python:3

RUN apt-get update \
  && apt-get install -y \
     vim \
     git 

WORKDIR /home

