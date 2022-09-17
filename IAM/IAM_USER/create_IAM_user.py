import boto3

iam = boto3.client('iam')
response = iam.create_user(UserName='IAM user name enter')

print('user created',response)