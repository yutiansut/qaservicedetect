#
import click
import pymongo
import pika
import os


@click.command()
@click.option('--mongoip', default='127.0.0.1')
@click.option('--mongoport', default=27017)
@click.option('--mqhost', default='127.0.0.1')
@click.option('--mqport', default=5672)
@click.option('--mquser', default='admin')
@click.option('--mqpwd', default='admin')
def detect(mongoip, mongoport, mqhost, mqport, mquser, mqpwd):
    print('detect mongo service')

    mongo = pymongo.MongoClient(
        host=mongoip, port=mongoport, serverSelectionTimeoutMS=1)
    mongo.test.test.find_one()
    print('mongo detect finished')

    print('detect rabbitmq service')
    credentials = pika.PlainCredentials(
        mquser, mqpwd, erase_on_connect=True)
    rabbitmqconnection = pika.BlockingConnection(
        pika.ConnectionParameters(host=mqhost, port=mqport,
                                  credentials=credentials, heartbeat=0, socket_timeout=5,
                                  )
    )
    print('rabbitmq detect finished')


