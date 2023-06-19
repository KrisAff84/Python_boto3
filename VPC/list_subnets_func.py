import boto3 


def list_subnets():
    ec2 = boto3.client('ec2')
    response = ec2.describe_subnets()
    for subnet in response['Subnets']:
        if 'Tags' in subnet:
            for tag in subnet['Tags']:
                if 'Name' == tag['Key']:
                    print(tag['Value'])
        print(subnet['SubnetId'])
        print(subnet['CidrBlock'])
        print(subnet['AvailabilityZone'])
        print(subnet['VpcId'])
        print()


def main():
    list_subnets()


if __name__ == '__main__':
    main()