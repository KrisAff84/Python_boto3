import boto3 


def create_vpc(cidr_block):
    ec2 = boto3.client('ec2')
    vpc = ec2.create_vpc(CidrBlock=cidr_block)
    print(vpc['Vpc']['VpcId'])
    return vpc

def main():
    cidr_block = '14.0.0.0/16'
    vpc = create_vpc(cidr_block)
    
if __name__ == '__main__':
    main()
    