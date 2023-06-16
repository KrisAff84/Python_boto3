import boto3

def delete_rt(rt_id):
    ec2 = boto3.client('ec2')
    response = ec2.delete_route_table(
    RouteTableId=rt_id
    )
    return response

def main():
    rt_id = 'rtb-02b42c39deb1ba3b2'
    delete_rt(rt_id)
    
if __name__ == '__main__':
    main()
