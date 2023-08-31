import boto3
import json


def stop_ec2_instance(InstanceID):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(
        InstanceIds=[
            InstanceID,
        ]
    )
    # if "'Code': 80, 'Name': 'stopped'" in response["StoppingInstances"][0]["CurrentState"]
    #     print("Instance is already stopped")

    if "stopped" in response["StoppingInstances"][0]["CurrentState"]["Name"]:
        print()
        print("Instance is already stopped")
        print()
    else:
        print(json.dumps(response, indent=4, default=str))


def main():
    
    InstanceID = 'i-0679ba0b2c3374832'
    stop_ec2_instance(InstanceID)

if __name__ == '__main__':
    main()
     