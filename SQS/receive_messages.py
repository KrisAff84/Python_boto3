import boto3


sqs = boto3.client('sqs')
response = sqs.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/835656321421/Time_Messages',
    MaxNumberOfMessages= 10,
    WaitTimeSeconds= 10,
)
    
try:
    for message in response["Messages"]:
            receipt_handle = message["ReceiptHandle"] 
            print("Message ID:", message["MessageId"])
            print("Body:", message["Body"])
            print()
            
            delete_response = sqs.delete_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/835656321421/Time_Messages',
            ReceiptHandle=receipt_handle
            )
except: 
    print('No messages in the queue')