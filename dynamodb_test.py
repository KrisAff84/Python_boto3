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
        },
        {
            'AttributeName': "Artist",
            'AttributeType': 'S',
        },
        {
            'AttributeName': "Year Released",
            'AttributeType': 'N',
        },

    ],
    KeySchema=[
        {
            'AttributeName': 'Title',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Artist',
            'KeyType': 'Range'
        },
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
