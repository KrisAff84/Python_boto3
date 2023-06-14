import boto3

s3 = boto3.client('s3')

# To filter objects returned use "Prefix"

response = s3.list_objects_v2(Bucket='kris-boto3-0834287', Prefix='Folder_A')

for content in response["Contents"]:
    print(content["Key"])
