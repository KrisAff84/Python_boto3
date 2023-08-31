import boto3 


region = 'us-west-1'

def start_docker_fleet(node1, node2, node3):
    ec2 = boto3.client('ec2', region_name=region)
    waiter = ec2.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[node1, node2, node3])
    response = ec2.start_instances(
        InstanceIds=[
            node1,
            node2,
            node3
        ],
    )

def get_public_ip(node1, config_file, line_number):
    print()
    print('Waiting for instances to start...')
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[node1])
    response = ec2.describe_instances(
        InstanceIds=[
            node1
        ],
    )
    print()
    for instance in response['Reservations']:
        print('Public IP of Node1:', instance['Instances'][0]['PublicIpAddress'])
        new_ip = instance['Instances'][0]['PublicIpAddress']

    with open(config_file, 'r') as file:
        lines = file.readlines()

    lines[line_number - 1] = f"    HostName {new_ip} \n"

    with open(config_file, 'w') as file:
        file.writelines(lines)  

    print()
    print('New IP of Node1 successfully written to config file')
    print()  


def main():
    node1='i-0679ba0b2c3374832'
    node2='i-0f2a756ed209bb8dc'
    node3='i-058847494653dd0ad'
    config_file='/Users/Kris/.ssh/config'
    line_number = 5
    start_docker_fleet(node1, node2, node3)
    get_public_ip(node1, config_file, line_number)


if __name__ == '__main__':
    main()
    
