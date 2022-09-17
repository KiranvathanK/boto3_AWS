#Describe Regions and Availability Zones
import boto3

ec2 = boto3.client('ec2','us-east-1')


response = ec2.describe_regions() 
print('Regions:', response['Regions'])

response = ec2.describe_availability_zones()  
print('Availability Zones:', response['AvailabilityZones'])