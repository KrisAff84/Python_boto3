import boto3

def list_object_keys(client, bucket, prefix=''):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:
        keys.append(content["Key"])
        
    return keys

