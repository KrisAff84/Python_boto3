import  boto3
ec2 = boto3.client('ec2')




def create_subnet(az, cidr_block, vpc_id):
    subnet = ec2.create_subnet(
        AvailabilityZone=az,
        CidrBlock=cidr_block,
        VpcId=vpc_id,
    )
    print(subnet['Subnet']['SubnetId']) 
    print(subnet['Subnet']['AvailabilityZone'])
    print(subnet['Subnet']['CidrBlock']) 
    print(subnet['Subnet']['VpcId']) 
    return subnet['Subnet']['SubnetId']
    
def main():
    az = 'us-east-1a'
    cidr_block = '12.0.1.0/24'
    vpc_id = 'vpc-0e361bdc46ddfad1c'
    
    create_subnet(az, cidr_block, vpc_id)
    
if __name__ = '__main__'
    main()