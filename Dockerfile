FROM sativiensiri/ubuntu-python3-flask:1.0

WORKDIR /app

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["flask-mongo.py"]

