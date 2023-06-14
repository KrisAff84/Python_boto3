# Uploads a new object

import boto3

s3 = boto3.client('s3')


bucket = 'kris-boto3-0834287'
key = 'Folder_A/trash.txt'
body = 'This is a trash text file' 


contenttype = 'string/plain'

s3.put_object(Bucket=bucket, Key=key, Body=body, ContentType=contenttype)
