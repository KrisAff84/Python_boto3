import boto3
import os

def create_keys(key_name, file_name):
    ec2 = boto3.client('ec2')
    response = ec2.create_key_pair(
        KeyName=key_name,
        )
    with open(file_name, 'w') as f:
        f.write(response['KeyMaterial'])
    os.chmod(file_name, 0o400)
    

def main():
    key_name = 'test2'
    file_ext = '.pem'
    file_name = (key_name + file_ext)
    create_keys(key_name, file_name)
    
    
if __name__ == '__main__':
    main()