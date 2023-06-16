import boto3
import json

ddb = boto3.client('dynamodb')
response = ddb.query(
    TableName='Songs',
    ExpressionAttributeValues={
        ':v1': {
            'S': 'Chris',
        },
    },
    KeyConditionExpression='Singer = :v1',
)

print(json.dumps(response, ensure_ascii=False, indent=2))
