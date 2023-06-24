import boto3
import json

sqs = boto3.client('sqs')

response = sqs.purge_queue(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/835656321421/Test_Messages'
)

print(json.dumps(response, indent=4, default=str))