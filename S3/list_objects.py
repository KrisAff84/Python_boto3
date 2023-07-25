import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='promotional-materials-9832732')

for content in response["Contents"]:
    print(content["Key"])

# Lists all objects in bucket    