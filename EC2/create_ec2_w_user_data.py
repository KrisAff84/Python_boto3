import boto3


def create_ec2_instance(ami, key_pair, sg_id, instance_type, subnet_id, user_data=None):
    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId=ami,
        InstanceType=instance_type,
        KeyName=key_pair,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            sg_id,
        ],
        SubnetId=subnet_id,
        UserData=user_data
    )

    print('Instance ID:', response['Instances'][0]['InstanceId'])
    if 'PublicIpAddress' in response['Instances'][0]:
        print('Public IP:', response['Instances'][0]['PublicIpAddress'])
    print('Private IP:', response['Instances'][0]['PrivateIpAddress'])
    if 'KeyName' in response['Instances'][0]:
        print('Key Pair Name:', response['Instances'][0]['KeyName'])
       
        
def main():
    ami = 'ami-053b0d53c279acc90'
    key_pair = 'boto3_key'
    sg_id = 'sg-0138eeb2f4568d5c0'
    instance_type = 't2.micro'
    subnet_id = 'subnet-0de0deccc117acb9a'
    user_data = '''#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctctl enable apache2
    echo "<h1>This is a test page from $(hostname -f)</h1>" > /var/www/html/index.html'''
    
    create_ec2_instance(ami, key_pair, sg_id, instance_type, subnet_id, user_data)
    
    
if __name__ == '__main__':
    main()