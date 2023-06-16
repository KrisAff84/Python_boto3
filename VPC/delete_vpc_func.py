import boto3 


def delete_vpc(vpc_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_vpc(
    VpcId=vpc_id,
)

def main():
    vpc_ids = ['vpc-0ccb94ff89463bbc1', 'vpc-0e361bdc46ddfad1c']
    for vpc_id in vpc_ids:
        delete_vpc(vpc_id)
   
    
if __name__ == '__main__':
    main()
    