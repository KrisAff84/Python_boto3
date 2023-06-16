import boto3

def list_route_tables(client):
    response = client.describe_route_tables()
    for routeTable in response['RouteTables']:
        print(routeTable['VpcId'])
        print(routeTable['RouteTableId'])
        for association in routeTable['Associations']:
            print(association['RouteTableAssociationId'])
            if 'SubnetId' in association:
                print(association['SubnetId'])
        for route in routeTable['Routes']:
            print(route['DestinationCidrBlock'])
            if 'GatewayId' in route:
                print(route['GatewayId'])
        print()
        
        
    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    list_route_tables(ec2)