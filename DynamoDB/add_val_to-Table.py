import boto3 

dynamodb = boto3.resource('dynamodb','us-east-1')
table = dynamodb.Table('employee')

table.put_item(
    Item={
        'username':'jd',
        'fname':'john',
        'lname':'deniel',
        'age':26,
        'gender':'male'
    }
)

print("item added:",table)
