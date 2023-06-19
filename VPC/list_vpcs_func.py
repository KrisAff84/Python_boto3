import boto3

def list_vpcs(filters=[]):
    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    print(tag['Value'])
        print(vpc['VpcId'])
        print(vpc['CidrBlock']) 
        print('Default VPC:', vpc['IsDefault'])
        print()

def get_vpc_name(filters=[]):
    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    print(tag['Value'])


def main():
    # filters=[{'Name': 'isDefault', 'Values': ['true']}]
    list_vpcs()  # returns all VPC
    # get_vpc_name(filters)  # returns all VPC names

                    
if __name__ == '__main__':
    main()
  
  

#######################################################
# Another way of doing it (not as clean imo)
# for vpc in response['Vpcs']:
#     print(vpc['VpcId'], vpc['CidrBlock'], 'Is default:', vpc['IsDefault'])
#     if 'Tags' in vpc:
#         for tag in vpc['Tags']:
#             if 'Name' == tag['Key']:
#                 print(tag['Value'])
#     print()