import boto3

def list_vpcs(client, filters=[]):
    response = client.describe_vpcs(Filters=filters)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    print(tag['Value'])
        print(vpc['VpcId'])
        print(vpc['CidrBlock']) 
        print('Default VPC:', vpc['IsDefault'])
        print()

def get_vpc_name(client, filters=[]):
    response = client.describe_vpcs(Filters=filters)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    print(tag['Value'])
                    
if __name__ == '__main__':
    list_vpcs(boto3.client('ec2'))  
    ec2 = boto3.client('ec2')
    filters=[{'Name': 'isDefault', 'Values': ['true']}]
        
    list_vpcs(ec2)  # returns all VPC
    
    list_vpcs(ec2, filters)  # Returns only default VPC
    
    get_vpc_name(ec2)  # returns all VPC names

#######################################################
# Another way of doing it (not as clean imo)
# for vpc in response['Vpcs']:
#     print(vpc['VpcId'], vpc['CidrBlock'], 'Is default:', vpc['IsDefault'])
#     if 'Tags' in vpc:
#         for tag in vpc['Tags']:
#             if 'Name' == tag['Key']:
#                 print(tag['Value'])
#     print()