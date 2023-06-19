import boto3


def delete_sg(sg_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_security_group(
        GroupId=sg_id
        )
    print(sg_id, 'Deleted')
    print(response)
        

def main():
    sg_id = 'sg-0138eeb2f4568d5c0'
    delete_sg(sg_id)
    
    
if __name__ == '__main__':
    main()
    