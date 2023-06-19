# Creates security group and adds rules
import boto3

# Create security group
def create_sg(group_name, description, vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.create_security_group(
    GroupName=group_name,
    Description=description,
    VpcId=vpc_id,
    )
    print(response['GroupId'])
    group_id = response['GroupId']
    return group_id
    

# Add rules to security group
# Hard code rules
def create_sg_ingress(group_id):
    ec2 = boto3.client('ec2')
    response = ec2.authorize_security_group_ingress(
        GroupId = group_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'SSH from all traffic',
                    },
                ],
                'ToPort': 22,
            },
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'HTTP from all traffic',
                    },
                ],
                'ToPort': 80,
            }
        ],
    )

    print(response)    

    
    
def main():
    group_name = 'test_sg'
    description = 'test_description'
    vpc_id = 'vpc-0f05385171fc81640'
    create_sg_ingress(create_sg(group_name, description, vpc_id))
    
    
if __name__ == '__main__':
    main()