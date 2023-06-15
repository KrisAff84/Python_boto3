import boto3
from list_object_keys_func import *

def filter_objects_ext(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
            
    return keys
    

if __name__ == "__main__":
    s3 = boto3.client('s3')
    
    response = list_object_keys(s3, "kris-boto3-0834287")
    print(response)
    
    response = filter_objects_ext(s3, "kris-boto3-0834287", "/")
    print(response)