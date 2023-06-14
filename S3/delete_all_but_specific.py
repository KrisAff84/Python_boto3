import boto3
from delete_objects import *
from get_object_functions import list_object_keys

s3 = boto3.client('s3')
bucket = 'kris-boto3-0834287'
prefix = 'Folder_A/folder1/'
keys = list_object_keys(s3, bucket, prefix=prefix)
print(keys)
keys = [key for key in keys if "/" not in key[len(prefix):]]
print(keys)
delete_objects(s3, bucket, keys)