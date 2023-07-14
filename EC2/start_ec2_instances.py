import boto3 
import json


def start_docker_fleet(node1, node2, node3):
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(
        InstanceIds=[
            node1,
            node2,
            node3
        ],
    )
    print(json.dumps(response, indent=4, default=str))


def get_ips(node1):
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[node1])
    response = ec2.describe_instances(
        InstanceIds=[
            node1
        ],
    )
    for instance in response['Reservations']:
        print('Pulbic IP of Node1:'['Instances'][0]['PublicIpAddress'])
    


def main():
    node1='i-05747a9d38a158d23'
    node2='i-06545abf9d8303298'
    node3='i-0259a1b93d8e0c690'
    start_docker_fleet(node1, node2, node3)

if __name__ == '__main__':
    main()