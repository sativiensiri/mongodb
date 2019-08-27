from mongoengine import *

connect(
    db="rabbitmq",
    username="rabbitmq",
    password="password",
    authentication_source="admin",
    host="10.44.94.135",
    port=27017
)
