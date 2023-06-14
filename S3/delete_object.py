# Deleting objects

import boto3

bucket = 'kris-boto3-0834287'
key = 'test_text.txt'
s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket=bucket,
    Key=key
    )

