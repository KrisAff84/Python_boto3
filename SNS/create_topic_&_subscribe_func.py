# Creates SNS topic and subscribes an email address

import boto3

def create_topic_subscribe(topic, email_address):
    sns = boto3.client('sns')
    response = sns.create_topic(
        Name=topic,
    )
        
    arn = response['TopicArn']
    
    response = sns.subscribe(
        TopicArn=arn,
        Protocol='email',
        Endpoint=email_address,
    )
    
    print('Topic ARN:', arn)
    print('Endpoint:', email_address)
    

def main():
    topic = 'test_topic'
    email_address = 'email_address@gmail.com'
    create_topic_subscribe(topic, email_address)
    

if __name__ == '__main__':
    main()
