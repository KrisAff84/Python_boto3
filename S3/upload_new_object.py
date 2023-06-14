# Uploads a new object

import boto3

s3 = boto3.client('s3')


bucket = "kris-boto3-0834287"
key = 'ProjectFiles/commands'
body = 'This file contains a list of commands to use for S3 in boto3: \n \
get_object \n \
list_objects \n \
list_objects_v2'  


contenttype = 'text/plain'

s3.put_object(Bucket=bucket, Key=key, Body=body, ContentType=contenttype)
