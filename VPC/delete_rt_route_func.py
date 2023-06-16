import boto3 


def delete_rt_route(dest_cidr, rt_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=rt_id,
    )
    return response
    

def main():
    dest_cidr = '0.0.0.0/0'
    rt_id = 'rtb-02b42c39deb1ba3b2'
    delete_rt_route(dest_cidr, rt_id)
    

if __name__ == "__main__":
    main()
