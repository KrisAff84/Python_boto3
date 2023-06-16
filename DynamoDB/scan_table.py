import boto3
import json

ddb = boto3.client('dynamodb')

response = ddb.scan(
    TableName='Songs',
    ReturnConsumedCapacity='TOTAL'
)

# print(response)

print(json.dumps(response, ensure_ascii=False, indent=2))

