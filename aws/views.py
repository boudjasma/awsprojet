from django.views.generic import View
from aws.models import Matter
from django.views.generic.list import ListView
import pandas as pd
from io import StringIO
from sqlalchemy import *
import boto3
from sqlalchemy.orm import sessionmaker

AccessKeyId = "AKIA44HNG66PEEIUS3Z5"
SecretAccessKey = "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"
bucket_name = "awsprojectgrp11s3"
filename = "matters.json"
path="/"


def connect_db():
    engine = create_engine("mysql://admin:user@name-db.cquuurrihevr.eu-west-3.rds.amazonaws.com:3306/testdb")
    return engine

def create_client():
    client = boto3.client('s3', aws_access_key_id=AccessKeyId, aws_secret_access_key=SecretAccessKey)
    return client


def local_to_S3(client, path):
    buffer = StringIO()
    data = pd.read_csv(path)
    data.to_csv(buffer)
    buffer.seek(0)
    response = client.put_object(Bucket='awsprojectgrp11s3', Body=buffer.getvalue(), Key='matters.json')
    return response['ResponseMetadata']['HTTPStatusCode']


def local_to_RDS(engine, path):
    df = pd.read_json(path)
    Session = sessionmaker(bind=engine)
    session = Session()
    meta = MetaData()
    meta.bind = engine
    df.to_sql(con=engine, name='matters')
    session.commit()
    return "ok"


def S3_to_local(bucket, path, client, object_name):
    client.download_file(bucket, object_name, path)


def S3_to_RDS(engine, client, bucket, path, object_name):
    S3_to_local(bucket, path, client, object_name)
    local_to_RDS(engine, path)

def RDS_to_S3(client,path):
    local_to_S3(client, path)

class MatterList(ListView):
    model = Matter

    def post(self, request, *args, **kwargs):
        if request.POST.get("s3_to_rds"):
            S3_to_RDS(connect_db, create_client(), bucket_name, path,filename)
        else:
            RDS_to_S3(create_client(),path)