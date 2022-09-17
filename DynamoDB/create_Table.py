import boto3

dynamodb = boto3.resource('dynamodb','us-east-1')

table = dynamodb.create_table(
    TableName='employee',
    KeySchema=[
        {
            'AttributeName':'fname',
            'KeyType':'HASH'
        },
        {
            'AttributeName':'lname',
            'KeyType':'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName':'fname',
            'AttributeType':'S'
        },
        {
            'AttributeName':'lname',
            'AttributeType':'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits':5,
        'WriteCapacityUnits':5
    }
)

table.wait_until_exists()

print(table.item_count)
