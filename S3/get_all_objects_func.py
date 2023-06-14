import boto3
import os
from get_object_functions import list_object_keys

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

def get_all_objects(client, bucket):
    keys = list_object_keys(client, bucket)
        
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(client, bucket, key, key)
                
client = boto3.client('s3')
bucket = 'kris-boto3-0834287'

get_all_objects(client, bucket)