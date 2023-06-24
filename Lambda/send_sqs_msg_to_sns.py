import boto3

sqs = boto3.client('sqs')
sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:835656321421:Email-Me'
queue_url = 'https://sqs.us-east-1.amazonaws.com/835656321421/Test_Messages'


def lambda_handler(event, context):
    context = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages= 1,
        WaitTimeSeconds= 10,
    )
        message_id = response['MessageId']
        body = response['Body']
        
        
    response = sns.publish(
        TopicArn=topic_arn,
        Message=body,
        Subject='Current Time',
    )
    
    return {
        'statusCode': 200,
        'body': body
    }
