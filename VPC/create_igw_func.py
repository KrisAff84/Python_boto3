import boto3


def create_igw():
    ec2 = boto3.client('ec2')
    igw = ec2.create_internet_gateway()
    print(igw['InternetGateway']['InternetGatewayId'])
    return igw['InternetGateway']['InternetGatewayId']

    
def main():
    create_igw()
    
    
if __name__ == '__main__':
    main()
    
    
