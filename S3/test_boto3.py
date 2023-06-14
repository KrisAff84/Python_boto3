import boto3

session = boto3.Session()

s3 = session.client('s3')
s3 = boto3.client('s3')

s3 = boto3.resource('s3')
s3 = session.resource('s3')

# Difference is level of extraction
# Client gives more API type response
# Resource provides python type response