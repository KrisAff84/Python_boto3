import boto3


def associate_subnets(rt_id, subnet_id):
    ec2 = boto3.client('ec2')
    association = ec2.associate_route_table(
        RouteTableId=rt_id,
        SubnetId=subnet_id
    )
    print(association['AssociationId'])
    return association['AssociationId']
    
    
def main():
    rt_id = 'rtb-02b42c39deb1ba3b2'
    subnet_id = 'subnet-07a29ae59db56da5b'
    associate_subnets(rt_id, subnet_id)
    

if __name__ == '__main__':
    main()
    