import boto3


def create_topic_subscribe(name, email_address):
    sns = boto3.client('sns')
    response = sns.create_topic(
        Name='test_topic',
    )
        
    arn = response['TopicArn'])
    
    response = sns.subscribe(
        TopicArn=arn,
        Protocol='email',
        Endpoint=email_address,
    )
    
    print(response)
    
