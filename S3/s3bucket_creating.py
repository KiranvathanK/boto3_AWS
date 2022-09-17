import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-bucketragner12022')

if s3.create_bucket:
    print("bucket created succesfully")
else:
    ("error")