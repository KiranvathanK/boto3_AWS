import boto3

cloudwatch = boto3.client('cloudwatch','us-east-1')
paginator = cloudwatch.get_paginator('describe_alarms')

for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response['MetricAlarms'])
    
