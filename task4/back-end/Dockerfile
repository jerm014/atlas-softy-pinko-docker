# don't use latest, use 22.04
FROM ubuntu:22.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN apt-get clean
RUN -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /app
COPY api.py /app/api.py
RUN pip3 install flask
RUN pip3 install flask-cors
EXPOSE 5252
#run the flask web server
CMD ["python3", "/app/api.py"]
