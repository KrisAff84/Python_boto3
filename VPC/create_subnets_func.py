import  boto3


def del_subnet(subnet_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_subnet(
        SubnetId=subnet_id
    )
    print('SubnetID:', subnet_id, 'deleted.')

    
def main():
    subnet_id = 'subnet-07a29ae59db56da5b'
    del_subnet(subnet_id)


if __name__ == '__main__':
    main()