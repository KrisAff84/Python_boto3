import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='kris-ssl-test-983272'
)

print(response)
