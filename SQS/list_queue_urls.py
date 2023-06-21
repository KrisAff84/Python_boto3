import boto3


def list_queue_urls():
    sqs = boto3.client('sqs', verify=False)
    response = sqs.list_queues()
    print('Queue URLs:')
    print(response['QueueUrls'])


def main():
    list_queue_urls()


if __name__ == '__main__':
    main()
