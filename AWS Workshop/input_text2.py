import os

print(os.getcwd())

my_file = open(os.path.join(os.getcwd(), 'Python_boto3/AWS Workshop/text.txt'), "r")

print(my_file.read())
