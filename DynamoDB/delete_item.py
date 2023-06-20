import boto3
import json


def delete_item(table, hash_key, hash_key_value, sort_key, sort_key_value):
    ddb = boto3.client('dynamodb')
    response = ddb.delete_item(
        TableName=table,
        Key={
            hash_key: {
                'S': hash_key_value,
            },
            sort_key: {
                'S': sort_key_value,
            },
        },
    )
    print(json.dumps(response, indent=4, default=str)) 
    

def main():
    table = 'Songs'
    hash_key = 'Singer'
    hash_key_value = 'Chris'
    sort_key = 'Song'
    sort_key_value = 'Brown Eyed Girl'
    delete_item(table, hash_key, hash_key_value, sort_key, sort_key_value)
    
    
if __name__ == '__main__':
    main()
    