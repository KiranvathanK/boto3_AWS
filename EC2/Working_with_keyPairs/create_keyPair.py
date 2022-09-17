import boto3

ec2 = boto3.client('ec2','us-east-1')
response = ec2.create_key_pair(KeyName='regionkey')
print("key created:",response)