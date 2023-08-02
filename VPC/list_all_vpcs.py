import boto3
import json

regions = ["us-east-1", "us-east-2", "us-west-1", "us-west-2"]


for region in regions:
    print(f'Region: {region}')
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_vpcs()
    for vpc in response['Vpcs']:
        print(json.dumps(vpc, indent=4))
        print()
