import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='kris-boto3-0834287')

# for content in response["Contents"]:
#     if '.txt' in content["Key"][-4:]: 
#         print(content["Key"])
        
        
extension = '.txt'

for content in response["Contents"]:
    if extension in content["Key"][-(len(extension)):]): 
        print(content["Key"])
