import boto3

def list_images(owner):
    ec2 = boto3.client('ec2')
    response = ec2.describe_images(
        Owners=[owner]
    )
    image_count = 0
    for image in response['Images']:
        print('AMI:', image['ImageId'])
        print('Name:', image['Name'])
        print('Creation Date:', image['CreationDate'])
        print('Location:', image['ImageLocation'])
        image_count += 1
        print()
    print('Total Images:', image_count)
    
def main():
    owner = 'self'
    list_images(owner)
    
    
if __name__ == '__main__':
    main()