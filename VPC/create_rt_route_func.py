import boto3 


def create_rt_route(dest_cidr, gw_id, rt_id):
    ec2 = boto3.client('ec2')
    response = ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=gw_id,
    RouteTableId=rt_id,
    )
    return response
    

def main():
    dest_cidr = '0.0.0.0/0'
    gw_id = 'igw-0bdc8c2fb487c5cd3'
    rt_id = 'rtb-02b42c39deb1ba3b2'
    create_rt_route(dest_cidr, gw_id, rt_id)
    

if __name__ == "__main__":
    main()