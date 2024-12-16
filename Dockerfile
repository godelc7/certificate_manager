FROM ubuntu:20.04
RUN apt update -y && \
    apt install python3-pip -y && \
    apt clean && \
    pip3 install Flask==2.2.2 pytest==7.1.2

WORKDIR /app
EXPOSE 5000
COPY . /app
CMD ["python3", "./main.py"]

