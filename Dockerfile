FROM python:3.10-slim-bullseye

COPY . /app

WORKDIR /app


RUN apt-get update -y && apt-get install libpq-dev build-essential python3-dev -y 


RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \ 
    chmod +x entrypoint.sh

# CMD ["/app/entrypoint.sh"]

 

