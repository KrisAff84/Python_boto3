import json
import boto3


def lambda_handler(event, context):
    bucket_name = "cf-templates-w6p9rrn8ltmr-us-west-1"
    s3 = boto3.client("s3")
    response = s3.list_objects(
        Bucket=bucket_name
    )
    
    contents = response['Contents']
    key_names = []
    
    for content in contents:
        print(content['Key'])
        key_names.append(content['Key'])
        
        
    return {
        'statusCode': 200,
        'body': json.dumps(key_names)
    }
    
