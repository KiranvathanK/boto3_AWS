import boto3

dynamodb = boto3.resource('dynamodb','us-east-1')
table = dynamodb.Table('employee')
response = table.get_item(
    Key={
        'fname':'john',
        'lname':'deniel'
    }
)

item = response['Item']
print(item)