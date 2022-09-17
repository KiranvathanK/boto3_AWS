import boto3

ec2 = boto3.client('ec2','us-east-1')
responce = ec2.describe_instances()
print(responce)