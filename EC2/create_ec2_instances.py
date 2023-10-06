import boto3


def create_ec2_instance(region, ami, key_pair, sg_id, instance_type, subnet_id):
    ec2 = boto3.client('ec2', region_name=region)
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
    )

    print('Instance ID:', response['Instances'][0]['InstanceId'])
    if 'PublicIpAddress' in response['Instances'][0]:
        print('Public IP:', response['Instances'][0]['PublicIpAddress'])
    print('Private IP:', response['Instances'][0]['PrivateIpAddress'])
    if 'KeyName' in response['Instances'][0]:
        print('Key Pair Name:', response['Instances'][0]['KeyName'])
       
        
def main():
    region = 'us-east-1'
    ami = 'ami-026ebd4cfe2c043b2'
    key_pair = 'boto3_key'
    sg_id = 'sg-0138eeb2f4568d5c0'
    instance_type = 't2.micro'
    subnet_id = 'subnet-0de0deccc117acb9a'
    create_ec2_instance(region, ami, key_pair, sg_id, instance_type, subnet_id)
    
    
if __name__ == '__main__':
    main()