import boto3


def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:835656321421:Current_Time'
    for message in event['Records']:
        body = message['body']
        print(body)
    
        sns_pub = sns.publish(
            TopicArn=topic_arn,
            Message=body,
            Subject='Current Time',
        )
    
    
    return {
        'statusCode': 200,
        'body': body
    }
