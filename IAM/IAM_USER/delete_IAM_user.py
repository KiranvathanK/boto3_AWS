import boto3

iam = boto3.client('iam')

response = iam.delete_user(UserName='enter a user name to delete')
print("enter user name has been deleted")