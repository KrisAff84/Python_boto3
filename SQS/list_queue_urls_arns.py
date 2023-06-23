import boto3


def list_queue_urls():
    sqs = boto3.client('sqs')
    response = sqs.list_queues()
    
    for entry in response['QueueUrls']:
        queuename = entry.split('/')[-1]            # Gets queue name from URL
        actnumber = entry.split('/')[-2]                # Gets act number from URL
        sqs_region = entry.split('/')[-3]                   # Gets 'sqs.<region>' from URL
        region = sqs_region.split('.')[1]                       # Removes 'sqs.' from region to get region by itself
        arn = f'arn:aws:sqs:{region}:{actnumber}:{queuename}'       # Pieces all variables together in ARN format
        
        print('Queue name:', queuename)
        print('Queue URL:', entry)
        print('Queue ARN:', arn)
        print()
      
    
def main():
    list_queue_urls()


if __name__ == '__main__':
    main()
