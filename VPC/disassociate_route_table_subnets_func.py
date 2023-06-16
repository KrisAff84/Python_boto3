# In order to disassociate route table the RouteTableAssociationID is needed
# The only way to get this information is programatically, therefore
# this function calls a function to get route table association ID before 
# disassociating route table

import boto3


def get_rt_assoc_id(rt_id):
    ec2 = boto3.client('ec2')
    response = ec2.describe_route_tables(
        RouteTableIds=[
            rt_id,
        ],
    )
    for assoc in response['RouteTables'][0]['Associations']:
        if not assoc['Main']:
            assoc_id = assoc['RouteTableAssociationId']
    return assoc_id
    
    
def disassociate_rt(assoc_id):
    ec2 = boto3.client('ec2')
    response = ec2.disassociate_route_table(
        AssociationId=assoc_id
        )
    return response
    
    
def main():
    rtt_id = 'rtb-02b42c39deb1ba3b2'
    disassociate_rt(get_rt_assoc_id(rtt_id))
    
    
if __name__ == '__main__':
    main()
    