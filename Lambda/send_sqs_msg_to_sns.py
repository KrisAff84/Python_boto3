import boto3



def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:835656321421:Email-Me'
    queue_url = 'https://sqs.us-east-1.amazonaws.com/835656321421/Test_Messages'
    event = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages= 1,
        WaitTimeSeconds= 10,
    )
    
    body = event["Messages"][0]["Body"]
        
        
    response = sns.publish(
        TopicArn=topic_arn,
        Message=body,
        Subject='Current Time',
    )
    
    return {
        'statusCode': 200,
        'body': body
    }
