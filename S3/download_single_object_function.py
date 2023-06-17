
import boto3
import os
from get_object_functions import list_object_keys

def download_single_object(bucket, key, filename):
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, filename)
    
if __name__ == '__main__':
        
    bucket = 'kris-boto3-0834287'
    key = 'test_text.txt'
    filename = key
    
    s3 = boto3.client('s3')
   
    keys = list_object_keys(s3, bucket)
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)
    