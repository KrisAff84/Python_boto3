# Delete multiple objects

import boto3
from get_object_functions import list_object_keys




bucket = 'kris-boto3-0834287'
key = 'test_text.txt'
s3 = boto3.client('s3')

def delete_objects(client, bucket, keys):
    
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects 
        }
    )
    
    return response

###############################################

bucket = 'kris-boto3-0834287'
s3 = boto3.client('s3')

delete_objects(s3, bucket, ['test_text_string.txt', 'test_text_upload.txt'])

################################################
# Deleting Folders

def delete_folders(client, bucket, prefix):
    
    keys = list_object_keys(client, bucket, prefix)
    
    return delete_objects(client, bucket, keys)
    bucket = 'kris-boto3-0834287'
    s3 = boto3.client('s3')
    
    keys = list_object_keys(s3, bucket, prefix="Folder_A/")
    delete_objects(s3, bucket, keys)