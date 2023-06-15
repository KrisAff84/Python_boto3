# Creates new bucket
import boto3


def bucket_create(bucket):
    s3 = boto3.client('s3')
    response = s3.create_bucket(
        Bucket=bucket 
    )
    return response

bucket_create('test-bucket-98374')
