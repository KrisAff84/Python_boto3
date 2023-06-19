import boto3


def delete_ami(ami_id):
    ec2 = boto3.client('ec2')
    response = ec2.deregister_image(
        ImageId=ami_id
        )
    print(ami_id, "Deleted")
    print(response)
    
    
def main():
    ami_id = 'ami-0363581eb95e86b74' 
    delete_ami(ami_id)
    
    
if __name__ == "__main__":
    main()