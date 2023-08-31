import boto3
import json


def stop_ec2_instances(Instance1, Instance2, Instance3):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(
        InstanceIds=[
            Instance1,
            Instance2,
            Instance3
        ]
    )
    print(json.dumps(response, indent=4, default=str))


def main():
    Instance1='i-0679ba0b2c3374832'
    Instance2='i-0f2a756ed209bb8dc'
    Instance3='i-058847494653dd0ad'
    stop_ec2_instances(Instance1, Instance2, Instance3)

if __name__ == '__main__':
    main()
    