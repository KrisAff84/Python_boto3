import boto3 


def detach_igw(igw_id, vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.detach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id
    )
    return response
    

def main():
    igw_id = 'igw-0bdc8c2fb487c5cd3'
    vpc_id = 'vpc-0e361bdc46ddfad1c'
    detach_igw(igw_id, vpc_id)
    

if __name__ == "__main__":
    main()
    
