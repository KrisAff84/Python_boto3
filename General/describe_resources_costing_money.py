import boto3
import json


regions = ["us-east-1", "us-east-2", "us-west-1", "us-west-2"]


class Format:
    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'


print()
print(f'{Format.blue_underline}*************** EC2 INSTANCES ***************{Format.end}')
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        print('Instance Name:', tag['Value'])
            print('Instance ID:', instance['InstanceId'])
            print('Instance Type:', instance['InstanceType'])
            print('AMI:', instance['ImageId'])
            print('State:', instance['State']['Name'])
            if 'VpcId' in instance:
                print('VPC ID:', instance['VpcId'])
            if 'SubnetId' in instance:
                print('Subnet ID:', instance['SubnetId'])
            print('Time Launched:', instance['LaunchTime'])
            for sg in instance['SecurityGroups']:
                print('Security Group ID:', sg['GroupId'])
                print('Security Group Name:', sg['GroupName'])
            if 'PrivateIpAddress' in instance:
                print('Private IP Address:', instance['PrivateIpAddress'])
            if 'PublicIpAddress' in instance:
                print('Public IP Address:', instance['PublicIpAddress'])
            if 'KeyName' in instance:
                print('Key Pair Name:', instance['KeyName'])
            if 'IamInstanceProfile' in instance:
                print('IAM Instance Profile ARN:', instance['IamInstanceProfile']['Arn'])
                print('IAM Instance Profile ID:', instance['IamInstanceProfile']['Id'])
            print()
print()
print(f'{Format.blue_underline}*************** ELASTIC IPS ***************{Format.end}')
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    eip = boto3.client('ec2', region_name=region)
    response = eip.describe_addresses()
    for address in response['Addresses']:
        if 'PublicIp' in address:
            print('Public IP:', address['PublicIp'])
            if 'PrivateIpAddress' in address:
                print('Private IP:', address['PrivateIpAddress'])
            if 'NetworkInterfaceId' in address:
                print('Network Interface ID:', address['NetworkInterfaceId'])
            print('Allocation ID:', address['AllocationId'])
            print('Domain:', address['Domain'])
            if 'InstanceId' in address:
                print('Instance ID:', address['InstanceId'])
            if 'AssociationId' in address:
                print('Association ID:', address['AssociationId'])
            if 'AssociationId' not in address:
                print('EIP is not associated!!!')
    print()
print()
print(f'{Format.blue_underline}*************** RDS SNAPSHOTS ***************{Format.end}')
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    rds = boto3.client('rds', region_name=region)
    response = rds.describe_db_snapshots()
    for snapshot in response['DBSnapshots']:
        if 'DBSnapshotIdentifier' in snapshot:
            print('Snapshot Name:', snapshot['DBSnapshotIdentifier'])
            print('Database Name:', snapshot['DBInstanceIdentifier'])
            print('ARN:', snapshot['DBSnapshotArn'])
            print('Snapshot Create time:', snapshot['SnapshotCreateTime'])
            print('Engine:', snapshot['Engine'])
            print('Allocated Storage:', snapshot['AllocatedStorage'], 'GB')
            print()
    print()