import boto3

def list_instance_types():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instance_types(
        Filters=[
            {
                'Name': 'free-tier-eligible',
                'Values': [
                    'true',
                ]
            },
        ],
    )

    for instanceType in response['InstanceTypes']:
        print(instanceType['InstanceType'], instanceType['FreeTierEligible'])
      
    
def main():
    list_instance_types()
    
    
if __name__ == '__main__':
    main()