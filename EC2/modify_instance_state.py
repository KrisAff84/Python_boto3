import boto3


def start_instances(instance_ids):
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(InstanceIds=instance_ids)
    print(instance_ids, 'Started')


def stop_instances(instance_ids):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(InstanceIds=instance_ids)
    print(instance_ids, 'Stopped')
    
    
def terminate_instances(instance_ids):
    ec2 = boto3.client('ec2')
    response = ec2.terminate_instances(InstanceIds=instance_ids)
    print(instance_ids, 'Terminated')
    
    
def main():
    instance_ids = ['i-030c7852fa46cc46f']
    terminate_instances(instance_ids)
    
    
if __name__ == '__main__':
    main()