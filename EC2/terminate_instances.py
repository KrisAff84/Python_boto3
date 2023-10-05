import boto3
import json


def terminate_instances(instance_ids=[]):
    ec2 = boto3.client('ec2')
    response = ec2.terminate_instances(
        InstanceIds = instance_ids
        )
    print(json.dumps(response, indent=4, default=str))


def main():
    instance_ids = ['i-07b9bc7dc0994ce46', 'i-0872672d57ec39b3a', 'i-029242cf135dd859f']
    terminate_instances(instance_ids)
    

if __name__ == '__main__':
    main()
    