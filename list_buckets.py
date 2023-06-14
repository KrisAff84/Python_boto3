import boto3

s3 = boto3.client('s3')

response = s3.list_buckets(verify=False)

buckets = response['Buckets']

for bucket in buckets:
    print(bucket["Name"], bucket["CreationDate"])
