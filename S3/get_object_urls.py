# Returns all object names and URLs in a bucket

import boto3
import json

bucket = 'promotional-materials-9832732'

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket=bucket)

for content in response["Contents"]:
    object = (content["Key"])
    url = "https://%s.s3.amazonaws.com/%s" % (bucket, object)
    print()
    print(object)
    print(url)
    print()
