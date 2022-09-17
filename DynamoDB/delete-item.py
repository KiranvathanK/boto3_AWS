import boto3

dynamodb = boto3.resource('dynamodb','us-east-1')
table = dynamodb.Table('employee')
response = table.delete_item(
    Key={
        'fname': 'john',
        'lname': 'deniel'
    }
)

print("the item deleted succesfully",response)