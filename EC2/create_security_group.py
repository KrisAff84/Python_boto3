import boto3


def create_sg(group_name, description, vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.create_security_group(
    GroupName=group_name,
    Description=description,
    VpcId=vpc_id,
    )
    print(response['GroupId'])
    
    
def main():
    group_name = 'test_sg'
    description = 'test_description'
    vpc_id = 'vpc-0f05385171fc81640'
    create_sg(group_name, description, vpc_id)
    
    
if __name__ == '__main__':
    main()
    