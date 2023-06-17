import boto3


def create_ami(name,description, instance_id):
    ec2 = boto3.client('ec2')
    response = ec2.create_image(
    Name='Test AMI',
    Description='boto3 test AMI',
    InstanceId='i-0a9f1125d6b91f6c6',
    )
    print(response['ImageId'])

def main():
    name = 'Test AMI'
    description = 'boto3 test AMI'
    instance_id = 'i-0a9f1125d6b91f6c6'
    create_ami(name, description, instance_id)
    
    
if __name__ == '__main__':
    main()
