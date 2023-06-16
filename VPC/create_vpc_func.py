import boto3 


def creat_vpc(cidr_block):
    ec2 = boto3.client('ec2')
    vpc = ec2.create_vpc(CidrBlock=cidr_block)
    print(vpc['Vpc']['VpcId'])
    return vpc

def main():
    vpc = creat_vpc('14.0.0.0/16')
    
if __name__ == '__main__':
    main()