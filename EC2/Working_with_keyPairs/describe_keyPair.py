import boto3

ec2 = boto3.client('ec2','us-east-1')
response = ec2.describe_key_pairs()
print(response)

