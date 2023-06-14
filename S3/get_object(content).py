# Gets object bytes, which is the same as contents

import boto3

s3 = boto3.client('s3')   # This is the client
bucket = 'kris-boto3-0834287'
key = 'test_text.txt'
response = s3.get_object(Bucket=bucket, Key=key)

object_content = response['Body'].read()
contents = object_content.decode('utf-8')

print(contents)