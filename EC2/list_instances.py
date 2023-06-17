import boto3

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        print('Instance Name:', tag["Value"]) 
            print('Instance ID:', instance["InstanceId"])
            print('Instance Type:', instance["InstanceType"])
            print('AMI:', instance["ImageId"])
            print('State:', instance["State"]["Name"])
            print('VPC ID:', instance["VpcId"])
            print('Subnet ID:', instance["SubnetId"])
            print('Time Launched:', instance["LaunchTime"])
            for sg in instance["SecurityGroups"]:
                print('Security Group ID:', sg["GroupId"])
                print('Security Group Name:', sg["GroupName"])
            print('Private IP Address:', instance["PrivateIpAddress"])
            if "PublicIpAddress" in instance:
                print('Public IP Address:', instance["PublicIpAddress"])
            if "KeyName" in instance:
                print('Key Pair Name:', instance["KeyName"])
            if "IamInstanceProfile" in instance:
                print('IAM Instance Profile ARN:', instance["IamInstanceProfile"]['Arn'])
                print('IAM Instance Profile ID:', instance["IamInstanceProfile"]['Id'])
            print()
            
 
def main():
    list_ec2_instances()
    
    
if __name__ == '__main__':
    main()
