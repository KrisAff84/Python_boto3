import boto3

s3 = boto3.client('s3')

with open("test_text.txt", 'rb') as f: # Opens file, saves in memory 
    s3.put_object(Bucket="kris-boto3-0834287", Key="test_text.txt", \
        Body=f, ContentType="text/plain")

# Body of file can also be recorded directly in Body parameter
# Example
# s3.put_object(Bucket="kris-boto3-0834287", Key="test_text_string.txt", \
#         Body='This is a string', ContentType="text/plain")