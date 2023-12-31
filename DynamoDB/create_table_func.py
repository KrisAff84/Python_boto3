import boto3
import json


def create_table(name, hashkey, rangekey):
    ddb = boto3.client('dynamodb')
    response = ddb.create_table(
        TableName=name,
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
    name = 'Messages'
    hash_key = 'Date'
    range_key = 'ID'
    create_table(name, hash_key, range_key)

    
if __name__ == '__main__':
    main()
    