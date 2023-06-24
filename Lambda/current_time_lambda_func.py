import boto3
import time


def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    current_time = []
    t = time.localtime()
    c_time = time.strftime('%a:%m:%d:%I:%M:%S:%p')
    current_time.append(c_time.split(':'))

    day = current_time[0][0]
    month = current_time[0][1]
    date = current_time[0][2]
    hour = current_time[0][3]
    minutes = current_time[0][4]
    seconds = current_time[0][5]
    am_pm = current_time[0][6]

    the_time_is = (f'The current date and time is:  {day} {month} {date}, {hour}:{minutes}:{seconds} {am_pm}')
    sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/835656321421/Test_Messages',
        MessageBody=the_time_is
    )

    return {
        'statusCode': 200,
        'body': the_time_is
    }
