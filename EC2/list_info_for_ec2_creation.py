import boto3


regions = [
    'us-east-1', 
    'us-east-2', 
    'us-west-1', 
    'us-west-2'
]


class Format:
    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'


for region in regions:
    print()
    print(f'{Format.blue}********************************************************************************{Format.end}')
    print(f'                              {Format.blue_underline}Region: {region}{Format.end}')
    print(f'{Format.blue}********************************************************************************{Format.end}')
    print()
    print()
    print(f'{Format.blue_underline}********************** Amazon Linux Images **********************{Format.end}')
    print()
    ec2 = boto3.client('ec2', region_name=region)
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
    
    print(f'{Format.blue_underline}********************** Key Pairs **********************{Format.end}')
    print()
    response = ec2.describe_key_pairs()
    for keypair in response['KeyPairs']:
        print(keypair['KeyName'])
        print(keypair['KeyPairId'])
        print()

    print(f'{Format.blue_underline}********************** VPCs **********************{Format.end}')
    print()
    response = ec2.describe_vpcs()
    for vpc in response['Vpcs']:
        print(f'{Format.blue_underline}VPC:{Format.end}')
        print()
        if "Tags" in vpc:
            print(f'Name: {vpc["Tags"][0]["Value"]}')
        else:
            print(f'Name: No Name Tag')
        print(f'VPC ID: {vpc["VpcId"]}')
        print(f'CIDR: {vpc["CidrBlock"]}')
        if vpc['IsDefault'] == True:
            print('Default: Yes')
        else:
            print('Default: No')
        print()

        print(f'    {Format.blue_underline}Subnets:{Format.end}')
        print()
        response = ec2.describe_subnets(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [
                        vpc['VpcId']
                    ]
                }
            ]
        )
        for subnet in response['Subnets']:
            if 'Tags' in subnet:
                for tag in subnet['Tags']:
                    if 'Name' == tag['Key']:
                        print(f'        Name: {tag["Value"]}')
            print(f'        Subnet ID: {subnet["SubnetId"]}')
            print(f'        CIDR: {subnet["CidrBlock"]}')
            print(f'        Availability Zone: {subnet["AvailabilityZone"]}')
            print()
        
        print(f'    {Format.blue_underline}Security Groups:{Format.end}')
        print()
        response = ec2.describe_security_groups(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [
                        vpc['VpcId']
                    ]
                }
            ]
        )
        for sg in response['SecurityGroups']:
            print(f'        {Format.blue}Security Group:{Format.end}')
            print()
            print(f'        Name: {sg["GroupName"]}')
            print(f'        ID: {sg["GroupId"]}')
            print(f'        Description: {sg["Description"]}')
            print()
            print(f'            {Format.blue}SG Rules:{Format.end}')
            print()
            for permissions in sg['IpPermissions']:
                if 'FromPort'in permissions:
                    print(f'                From Port: {permissions["FromPort"]}')
                if 'ToPort' in permissions:
                    print(f'                To Port: {permissions["ToPort"]}')
                if 'IpProtocol' in permissions:
                    print(f'                Protocol: {permissions["IpProtocol"]}')
                if 'IpRanges' in permissions:
                    print(f'                Ip Ranges: {permissions["IpRanges"]}')
                print()
            print()
            print(f'        {Format.blue}***********************************{Format.end}')
            print()
        print(f'{Format.blue}*******************************************{Format.end}')
        print()
        


        
        