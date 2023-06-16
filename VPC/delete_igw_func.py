import boto3


def delete_igw(igw_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_internet_gateway(
        InternetGatewayId=igw_id)
    return response

    
def main():
    igw_id = 'igw-0bdc8c2fb487c5cd3'
    delete_igw(igw_id)
    
    
if __name__ == '__main__':
    main()
    