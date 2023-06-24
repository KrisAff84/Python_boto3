# Creates SNS topic and subscribes as many email addresses as are entered into list 'email_addresses'

import boto3

def create_topic_subscribe(topic, email_addresses):
    sns = boto3.client('sns')
    response = sns.create_topic(
        Name=topic,
    )
        
    arn = response['TopicArn']
    
    for email_address in email_addresses:
        response = sns.subscribe(
            TopicArn=arn,
            Protocol='email',
            Endpoint=email_address,
        )
    
    print('Topic ARN:', arn)
    print('Endpoints:', email_addresses)
    

def main():
    topic = 'test_topic'
    email_addresses = ['email_address1@gmail.com', 'email_address2@hotmail.com', 'email_address3@gmail.com']
    create_topic_subscribe(topic, email_addresses)
    

if __name__ == '__main__':
    main()
