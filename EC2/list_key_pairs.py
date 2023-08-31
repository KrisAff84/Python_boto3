import boto3


class Format:
    end = '\033[0m'
    blue_underline = '\033[34;4;1m'
    blue = '\033[34m'


def list_key_pairs(regions):
    for region in regions:
        print(f'{Format.blue_underline}Region:{Format.end} {Format.blue}{region}{Format.end}')
        print()
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_key_pairs()
        for keypair in response['KeyPairs']:
            print(keypair['KeyName'])
            print(keypair['KeyPairId'])
            print()
    

def main():
    regions = ['us-east-1','us-east-2','us-west-1','us-west-2']
    list_key_pairs(regions)
    
    
if __name__ == '__main__':
    main()