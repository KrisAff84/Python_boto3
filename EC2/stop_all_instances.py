# Stops all running EC2 intances from a list of regions

import boto3

regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']


def stop_all_instances():
    print()
    for region in regions:
        instance_ids = []
        total_instances = 0
        ec2 = boto3.client('ec2', region_name=region)
        instances = ec2.describe_instances()
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'running':
                    instance_ids.append(instance['InstanceId'])
                    total_instances += len(instance_ids)
        
        if len(instance_ids) > 0:
            ec2.stop_instances(InstanceIds=instance_ids)
            print(f'Stopping instances in {region}: {instance_ids}')
            print()
        else: 
            print(f'No instances running in {region}')
            print()
   

def main():
    stop_all_instances()


if __name__ == '__main__':
    main()
