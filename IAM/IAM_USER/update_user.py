import boto3

iam = boto3.client('iam')
response = iam.update_user(UserName = 'enter exist user name',
                           NewUserName = 'enter new user name to update')
print('the new user name is updated',response)