FROM python

RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list && rm -Rf /var/lib/apt/lists/* && apt-get update

RUN apt-get update && apt-get -y install ffmpeg libavcodec-extra && pip install pydub