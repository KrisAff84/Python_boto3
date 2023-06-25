import boto3


sqs = boto3.client('sqs')
response = sqs.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/835656321421/Time_Messages',
    MaxNumberOfMessages= 10,
    WaitTimeSeconds= 10,
)
    
# for message in response["Messages"]:
#     print("Message ID:", message["MessageId"])
#     print("Body:", message["Body"])
#     print()
    
print(response)
