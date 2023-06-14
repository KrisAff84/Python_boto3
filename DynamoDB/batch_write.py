import boto3


# Needs to be edited
def batch_write():
    ddb = boto3.client('dynamodb')
    response = dbb.batch_write_item(
        RequestItems={
            'string': [
                {
                    'PutRequest': {
                        'Item': {
                            'string': {
                                'S': 'string',
                                'N': 'string',
                                'B': b'bytes',
                                'SS': [
                                    'string',
                                ],
                                'NS': [
                                    'string',
                                ],
                                'BS': [
                                    b'bytes',
                                ],
                                'M': {
                                    'string': {'... recursive ...'}
                                },
                                'L': [
                                    {'... recursive ...'},
                                ],
                                'NULL': True|False,
                                'BOOL': True|False
                            }
                        }
                    },
  
                },
            ]
        },
        ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
        ReturnItemCollectionMetrics='SIZE'|'NONE'
)