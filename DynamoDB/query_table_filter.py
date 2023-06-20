import boto3
import json


def query_table_filter(singer, review='Review'):
    ddb = boto3.client('dynamodb')
    response = ddb.query(
        TableName='Songs',
        KeyConditionExpression='Singer = :singer',
        FilterExpression= 'Review = :review',
        ExpressionAttributeValues={
            ':singer': {
                'S': singer,
            },
            ':review': {
                'S': review,
            },
        },
    )
    
    print(json.dumps(response, ensure_ascii=False, indent=4))
    
    
def main():
    singer = 'Eundo'
    query_table_filter(singer)
    

if __name__ == '__main__':
    main()