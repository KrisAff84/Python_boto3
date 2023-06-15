import boto3
from delete_objects import *
from get_object_functions import *

def delete_non_recursive(client, bucket, prefix):
    keys = list_object_keys(client, bucket, prefix=prefix)
    print(keys)
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    print('Keys to be deleted: ', keys)
    response = delete_objects(s3, bucket, keys)
    return response
    
    
s3 = boto3.client('s3')
bucket = 'kris-boto3-0834287'
prefix = 'Folder_B/'

delete_non_recursive(s3, bucket, prefix)    
    