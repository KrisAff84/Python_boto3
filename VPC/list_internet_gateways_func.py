import boto3

ec2 = boto3.client('ec2')

def list_igws(client):
    response = client.describe_internet_gateways()
    for ig in response['InternetGateways']:
        print(ig['InternetGatewayId'])
        for att in ig['Attachments']:
            print(att['VpcId'])
            print(att['State'])
        print()


if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    list_igws(ec2)