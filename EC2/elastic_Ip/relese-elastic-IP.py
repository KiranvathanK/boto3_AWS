import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2','us-east-1')

try:
    response = ec2.release_address(AllocationId='enter hear allocation id of elasticIP')
    print("elastic ip released")
    
except ClientError as error:
    print(error)