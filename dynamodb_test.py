import boto3

ddb = boto3.client('dynamodb')

response = ddb.create_table(
    TableName='Songs',
    AttributeDefinitions=[
        {
            'AttributeName': "Title",
            'AttributeType': 'S',
        },
        {
            'AttributeName': "Key",
            'AttributeType': 'S',
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'Title',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Key',
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
