import boto3 

ec2 = boto3.client('ec2')

def list_subnets(client):
    response = client.describe_subnets()
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

if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    list_subnets(ec2)