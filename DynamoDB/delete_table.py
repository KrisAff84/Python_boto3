import boto3
import json

def delete_table(table_name):
    dbb = boto3.client('dynamodb')
    response = dbb.delete_table(
    TableName=table_name
    )
    print(json.dumps(response, indent=2))

def main():
    delete_table('Songs') # Enter the name of the table you wish to delete
    
if __name__ == '__main__':
    main()