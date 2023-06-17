import boto3
import json

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
    )
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])
            print(instance["InstanceType"])
            print(instance["ImageId"])
            print(instance["State"]["Name"])
            print(instance["VpcId"])
            print(instance["SubnetId"])
            print(instance["LaunchTime"])
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        print(tag["Value"]) 
            for sg in instance["SecurityGroups"]:
                print(sg["GroupId"])
                print(sg["GroupName"])
            print(instance["PrivateIpAddress"])
            if "PublicIpAddress" in instance:
                print(instance["PublicIpAddress"])
            if "KeyName" in instance:
                print(instance["KeyName"])
            if "IamInstanceProfile" in instance:
                print(instance["IamInstanceProfile"])
            print(" ")
            
 
def main():
    list_ec2_instances()
    
    
if __name__ == '__main__':
    main()
