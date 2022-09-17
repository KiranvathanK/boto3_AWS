import boto3 

dynamodb = boto3.resource('dynamodb','us-east-1')

table = dynamodb.Table('employee')

response = table.update_item(
    Key={
        'fname': 'john',
        'lname': 'deniel'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 28
    }
)