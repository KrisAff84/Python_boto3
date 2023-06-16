import boto3

def create_rt(vpc_id):
    ec2 = boto3.client('ec2')
    routeTable = ec2.create_route_table(VpcId=vpc_id)
    print(routeTable['RouteTable']['RouteTableId'])
    return routeTable['RouteTable']['RouteTableId']

def main():
    vpc_id = 'vpc-0e361bdc46ddfad1c'
    create_rt(vpc_id)
    
if __name__ == '__main__':
    main()