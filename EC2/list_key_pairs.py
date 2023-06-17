import boto3


def list_key_pairs():
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    for keypair in response['KeyPairs']:
        print(keypair['KeyName'])
        print(keypair['KeyPairId'])
        print()
    

def main():
    list_key_pairs()
    
    
if __name__ == '__main__':
    main()