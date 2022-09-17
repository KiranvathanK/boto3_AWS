import boto3

ec2 = boto3.client('ec2','us-east-1')
filters = [
    {
        'Name':'Domain',
        'Values':['vpc']
    }
]

response = ec2.describe_addresses(Filters=filters)
print(response)