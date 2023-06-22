# Stops EC2 instances without "SPECIAL_EXCEPTION" tag
# Sends email through SNS topic
import json
import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    ec2_instance_id = event['detail']['instance-id']
    tag_response = ec2.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [
                ec2_instance_id,
            ]
        },
    ],
    )
    
    alltags = tag_response['Tags']
    
    flag = 'STOP'
    for item in alltags:
        print(item['Key'])
        if item['Key'] == 'SPECIAL_EXCEPTION':
            flag = 'DONT_STOP'
            break
        
    print(flag)
    
    if flag == 'STOP':
        response = ec2.stop_instances(
            InstanceIds=[
            ec2_instance_id
            ]
        )
        
        snsarn = 'arn:aws:sns:us-east-1:835656321421:Email-Me'
        errormsg = 'EC2 ' + ec2_instance_id + ' Stopped'
        snsresponse = sns.publish(
        TopicArn=snsarn,
        Message=errormsg,
        Subject='EC2 violated company policy! Manager will be notified!',
        )

    
    
    
    return{
        'statusCode': 200, 
        'body': json.dumps('Hello, world!')
    }