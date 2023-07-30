import boto3
import json


def stop_ec2_instance(InstanceID):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(
        InstanceIds=[
            InstanceID,
        ]
    )
    print(json.dumps(response, indent=4, default=str))


def main():
    
    InstanceID = 'i-07e199db2c4d792d4'
    stop_ec2_instance(InstanceID)

if __name__ == '__main__':
    main()
     