import boto3
import json

ddb = boto3.client('dynamodb')

response = ddb.scan(
    TableName='Songs',
    ReturnConsumedCapacity='TOTAL'
)

print(json.dumps(response, indent=2))

