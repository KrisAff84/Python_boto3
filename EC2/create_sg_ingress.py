
import boto3


def create_sg_ingress(group_id):
    ec2 = boto3.client('ec2')
    response = ec2.authorize_security_group_ingress(
        GroupId = group_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'SSH from all traffic',
                    },
                ],
                'ToPort': 22,
            },
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'HTTP from all traffic',
                    },
                ],
                'ToPort': 80,
            }
        ],
    )

    print(response)
    
    
def main():
    group_id = 'sg-0ccd1534acc5c9721'
    create_sg_ingress(group_id)
    
    
if __name__ == '__main__':
    main()
    