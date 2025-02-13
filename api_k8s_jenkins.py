import boto3

ec2 = boto3.client('ec2')

instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, Type: {instance['InstanceType']}")
        