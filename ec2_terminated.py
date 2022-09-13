import boto3

ec2 = boto3.resource('ec2','us-east-1')
instances = ec2.instances.filter(Filters=
                                 [{
                                     'Name':'instance-state-name',
                                     'Values':['terminated']
                                    }]
                                 )

for instance in instances:
       print (instance.id, instance.instance_type)