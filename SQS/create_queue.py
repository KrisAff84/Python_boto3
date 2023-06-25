import boto3
import json


def create_queue(name):
    sqs = boto3.client('sqs')
    response = sqs.create_queue(
        QueueName=name,
        Attributes={
            'ReceiveMessageWaitTimeSeconds': '10'
        }
    )
    print(json.dumps(response, indent=4, default=str))
    return response


def main():
    name = 'Time_Messages'
    create_queue(name)


if __name__ == '__main__':
    main()
