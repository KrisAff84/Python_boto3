import boto3
import json

def delete_table(table_name):
    dbb = boto3.client('dynamodb')
    response = dbb.delete_table(
    TableName=table_name
    )
    print(json.dumps(response, indent=2))

def main():
    table_name = 'Songs'
    delete_table(table_name)
    
if __name__ == '__main__':
    main()