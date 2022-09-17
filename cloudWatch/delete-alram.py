import boto3

cloudwatch = boto3.client('cloudwatch','us-east-1')
response = cloudwatch.delete_alarms(
    AlarmNames=['Web_Server_CPU_Utilization'],
)