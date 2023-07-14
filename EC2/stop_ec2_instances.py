import boto3
import json


def stop_ec2_instances(Instance1, Instance2, Instance3):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(
        InstanceIds=[
            Instance1,
            Instance2,
            Instance3
        ],
    )
    print(json.dumps(response, indent=4, default=str))


def main():
    Instance1='i-05747a9d38a158d23'
    Instance2='i-06545abf9d8303298'
    Instance3='i-0259a1b93d8e0c690'
    stop_ec2_instances(Instance1, Instance2, Instance3)

if __name__ == '__main__':
    main()
    