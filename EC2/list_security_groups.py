import boto3


def list_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups(
        # Filters=[
        #     {
        #         'Name': 'vpc-id',
        #         'Values': [
        #             'vpc-0b5e4f154b9d81d02'
        #         ]
        #     }
        # ]
    )
    for sg in response['SecurityGroups']:
        print('*************************************************************')
        print()
        print('Name:',sg['GroupName'])
        print('ID:', sg['GroupId'])
        print('VPC:', sg['VpcId'])
        print()
        print('*** Security Group Rules ***')
        for permissions in sg['IpPermissions']:
            if 'FromPort'in permissions:
                print('From Port:', permissions['FromPort'])
            if 'ToPort' in permissions:
                print('To Port:', permissions['ToPort'])
            if 'IpProtocol' in permissions:
                print('Protocol:', permissions['IpProtocol'])
            if 'IpRanges' in permissions:
                print('Ip Ranges:', permissions['IpRanges'])
            print()
        print('Description:', sg['Description'])
        print()
        print()
        
        
def main():
    list_security_groups()
    
    
if __name__ == '__main__':
    main()