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

def replace_public_ip(instanceID, config_file, line_number):
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
        new_ip = instance['Instances'][0]['PublicIpAddress']    

    with open(config_file, 'r') as file:
        lines = file.readlines()

    lines[line_number - 1] = f"    HostName {new_ip} \n"

    with open(config_file, 'w') as file:
        file.writelines(lines)

    print()
    print('New IP of instance successfully written to config file')
    print()

def main():
    instanceID='i-05747a9d38a158d23'
    config_file='/Users/Kris/.ssh/config'
    line_number = 5
    start_instance(instanceID)
    replace_public_ip(instanceID, config_file, line_number)


if __name__ == '__main__':
    main()
    