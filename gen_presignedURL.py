import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', \
Params={'Bucket': 'kris-boto3-0834287', 'Key': 'test_text_string.txt'}, \
ExpiresIn=600)
        
print(response)