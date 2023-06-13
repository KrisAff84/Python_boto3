import boto3

s3 = boto3.client('s3')

s3.download_file('kris-boto3-0834287', 'test_text.txt', 'test_text.txt')
