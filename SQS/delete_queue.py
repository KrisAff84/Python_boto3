import boto3
import json


def delete_queue(url):
    sqs = boto3.client('sqs')
    response = sqs.delete_queue(
        QueueUrl=url
    )
    print(json.dumps(response, indent=4))


def main():
    url = ''
    delete_queue(url)


if __name__ == '__main__':
    main()
