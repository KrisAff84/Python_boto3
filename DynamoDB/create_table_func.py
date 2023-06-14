import boto3

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

create_table('Movies', 'Title', 'Year Released')