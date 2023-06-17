import boto3
import json

def create_table(name, hashkey, rangekey):
    ddb = boto3.client('dynamodb')
    response = ddb.create_table(
        TableName=name,
        AttributeDefinitions=[
            {
                'AttributeName': hashkey,
                'AttributeType': 'S',
            },
            {
                'AttributeName': rangekey,
                'AttributeType': 'S',
            }
        ],
        KeySchema=[
            {
                'AttributeName': hashkey,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': rangekey,
                'KeyType': 'RANGE'
            }
        ],
        BillingMode='PROVISIONED',
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
        StreamSpecification={
            'StreamEnabled': False,
        },
        TableClass='STANDARD',
    )
    print(json.dumps(response, indent=4, default=str))

def main():
    create_table('Songs', 'Singer', 'Song')
    
if __name__ == '__main__':
    main()