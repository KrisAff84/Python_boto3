import boto3


regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']


class Format:
    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'


print()
print(f'{Format.blue_underline}********************** Amazon Linux Images **********************{Format.end}')
print()
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_images(
        # Owners=[
        # 'amazon',
        # ],
        Filters=[
        {
            'Name': 'name',
            'Values': [
                'al2023-ami-2023.1.20230809.0-kernel-6.1-x86_64',
                'al2023-ami-2023.1.20230809.0-kernel-6.1-arm64',
                'amzn2-ami-kernel-5.10-hvm-2.0.20230727.0-x86_64-gp2',
                'amzn2-ami-kernel-5.10-hvm-2.0.20230727.0-arm64-gp2'           
            ]
        },
    ],
    )
    for image in response['Images']:
        print('Image ID:', image['ImageId'])
        print('Image Name:', image['Name'])
        print('Architecture:', image['Architecture'])
        print()

print(f'{Format.blue_underline}********************** Ubuntu Images **********************{Format.end}')
print()
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_images(
        # Owners=[
        # 'amazon',
        # ],
        Filters=[
        {
            'Name': 'name',
            'Values': [
                'ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230516',
                'ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-arm64-server-20230516',
                'ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20230517',
                'ubuntu/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20230517'           
            ]
        },
    ],
    )
    for image in response['Images']:
        print('Image ID:', image['ImageId'])
        print('Image Name:', image['Name'])
        print('Architecture:', image['Architecture'])
        print()