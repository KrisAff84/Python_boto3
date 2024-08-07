''' This script lists some of the most commonly used free tier AMIs in each region.
    Any number of regions can be added to the regions list, and the script will iterate through each. 

    The script can also be modified to list other AMIs, either not in the free tier, or other free tier AMIs.

    Currently, the script lists the following images:

    Amazon Linux
    Ubuntu
    SUSE Linux
    Red Hat

    When available, both x86_64 and arm64 images are listed.
'''

import boto3


class Format:
    '''
    This class is used to format the output of the script.
    '''

    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'

profile = input(f"{Format.blue}\nAWS profile:{Format.end} ")
session = boto3.Session(profile_name=profile)

regions = input(f"{Format.blue}\nRegions to list (Space separated. Press Enter for all US regions):{Format.end} ").split(' ')
if '' in regions:
    regions = [
        'us-east-1',
        'us-east-2',
        'us-west-1',
        'us-west-2'
    ]
print()
print(f'{Format.blue_underline}********************** Amazon Linux Images **********************{Format.end}')
print()
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = session.client('ec2', region_name=region)
    response = ec2.describe_images(
        Filters=[
        {
            'Name': 'name',
            'Values': [
                'al2023-ami-2023.1.20230809.0-kernel-6.1-x86_64',
                'al2023-ami-2023.1.20230809.0-kernel-6.1-arm64',
                'amzn2-ami-kernel-5.10-hvm-2.0.20230727.0-x86_64-gp2',
                'amzn2-ami-kernel-5.10-hvm-2.0.20230727.0-arm64-gp2',
                'amzn2-x86_64-MATEDE_DOTNET-2022.08.31'           
            ]
        },
    ],
    )
    for image in response['Images']:
        print('Image ID:', image['ImageId'])
        print('Image Name:', image['Name'])
        print('Description:', image['Description'])
        print('Architecture:', image['Architecture'])
        print()

print(f'{Format.blue_underline}********************** Ubuntu Images **********************{Format.end}')
print()
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = session.client('ec2', region_name=region)
    response = ec2.describe_images(     
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
        print('Description:', image['Description'])
        print('Architecture:', image['Architecture'])
        print()

print(f'{Format.blue_underline}********************** SUSE Linux Images **********************{Format.end}')
print()
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = session.client('ec2', region_name=region)
    response = ec2.describe_images(
        Filters=[
        {
            'Name': 'name',
            'Values': [
                'suse-sles-15-sp5-v20230620-hvm-ssd-x86_64',
                'suse-sles-15-sp5-v20230620-hvm-ssd-arm64',
                'suse-sles-12-sp5-v20230206-hvm-ssd-x86_64'          
            ]
        },
    ],
    )
    for image in response['Images']:
        print('Image ID:', image['ImageId'])
        print('Image Name:', image['Name'])
        print('Description:', image['Description'])
        print('Architecture:', image['Architecture'])
        print()

print(f'{Format.blue_underline}********************** Red Hat Images **********************{Format.end}')
print()
for region in regions:
    print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
    ec2 = session.client('ec2', region_name=region)
    response = ec2.describe_images(
        Filters=[
        {
            'Name': 'name',
            'Values': [
                'RHEL-9.2.0_HVM-20230503-x86_64-41-Hourly2-GP2',
                'RHEL-9.2.0_HVM-20230503-arm64-41-Hourly2-GP2'           
            ]
        },
    ],
    )
    for image in response['Images']:
        print('Image ID:', image['ImageId'])
        print('Image Name:', image['Name'])
        print('Description:', image['Description'])
        print('Architecture:', image['Architecture'])
        print()
        