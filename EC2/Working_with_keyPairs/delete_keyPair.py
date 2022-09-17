import boto3

ec2 = boto3.client('ec2','us-east-1')
response = ec2.delete_key_pair(KeyName="regionkey")
print('the key is delated',response)