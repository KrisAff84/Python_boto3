import boto3


sessions = ['admin-profile', 'lyria_dev']

for session in sessions:
    session = boto3.Session(profile_name=session)
    s3 = session.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])