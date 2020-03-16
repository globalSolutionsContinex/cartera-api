FROM python:3.6-stretch

ENV FLASK_ENV = production

RUN apt-get update

COPY . /var/www
WORKDIR /var/www

RUN pip3 install -r requirements.txt
RUN chmod +x run.sh

EXPOSE 5000

CMD ["python3", "main.py"]
