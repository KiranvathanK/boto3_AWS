import boto3

dynamodb = boto3.resource('dynamodb','us-east-1')
table = dynamodb.Table('employee')

print('table',table.creation_date_time)