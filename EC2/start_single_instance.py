import boto3 


def start_instance(instanceID):
    
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[instanceID])
    response = ec2.start_instances(
        InstanceIds=[
            instanceID
        ],
    )

def get_public_ip(instanceID):
    print()
    print('Waiting for instance to start...')
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instanceID])
    response = ec2.describe_instances(
        InstanceIds=[
            instanceID
        ],
    )
    print()
    for instance in response['Reservations']:
        print('Public IP of Instance:', instance['Instances'][0]['PublicIpAddress'])    


def main():
    instanceID = 'i-07e199db2c4d792d4'
    start_instance(instanceID)
    get_public_ip(instanceID)


if __name__ == '__main__':
    main()
    