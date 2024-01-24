'''
This script will show the contents of an S3 bucket, and ask user for a key to replace. 
The script will then ask for the path to the new file, and replace the file in the bucket.
'''

import boto3
from datetime import datetime

session = boto3.Session(profile_name='admin-profile')
bucket_name = 'my-resume-kris'

s3 = session.client('s3')
print()
print("Current files the bucket: ")
print()
response = s3.list_objects_v2(Bucket=bucket_name)

for content in response['Contents']:
    print(content['Key'])

bucket_key = input("Enter the bucket key you want to replace: ")
file_path = input("Enter the path to the new file: ")

s3.delete_object(Bucket=bucket_name, Key=bucket_key)
s3.upload_file(file_path, bucket_name, bucket_key)
print('File replaced successfully')
