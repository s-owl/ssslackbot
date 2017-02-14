FROM python:latest

MAINTAINER Harvey Kim <vaporize93@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y

# Timezone
ENV TZ=Asia/Seoul
RUN echo $TZ | tee /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata


ADD requirements.txt /src/
WORKDIR /src
RUN pip install -r requirements.txt

ADD run.py slackbot_settings.py /src/
ADD plugins /src/plugins

CMD ["python", "./run.py"]
