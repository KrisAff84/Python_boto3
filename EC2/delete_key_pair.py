import boto3
import os


def delete_keys(key_name, file_name):
    ec2 = boto3.client('ec2')
    response = ec2.delete_key_pair(
        KeyName=key_name,
        )
    if os.path.isfile(file_name):
        os.remove(file_name)
    print(key_name, 'Deleted')
  
 
def main():
    key_name = 'test_key'
    file_ext = '.pem'
    file_name = (key_name + file_ext)
    delete_keys(key_name, file_name)
    
    
if __name__ == '__main__':
    main()
