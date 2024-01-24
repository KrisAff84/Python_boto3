import boto3
import json


def describe_instance_with_tags(region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Type',
                'Values': [
                    'ansible'
                ]
            }
        ]
    )
    print(json.dumps(response, indent=4, default=str))
    public_ips = []
    instance_ids = []
    for instance in response['Reservations']:
        public_ips.append(instance['Instances'][0]['PublicIpAddress'])
        instance_ids.append(instance['Instances'][0]['InstanceId'])
    
    count = 0
    for id in instance_ids:
        print(f"Instance {count + 1}: {id}   {public_ips[count]}")
        count += 1




def main():
    region = 'us-west-2'
    describe_instance_with_tags(region)


if __name__ == '__main__':
    main()