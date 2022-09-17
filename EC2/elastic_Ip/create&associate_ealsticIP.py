import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2','us-east-1')

try:
    allocation = ec2.allocate_address(Domain='vpc')
    response = allocation.associate_address(AllocationId=allocation['AllocationId'],InstanceId='enter instace-id')
    print(response)
except ClientError as e:
    print(e)