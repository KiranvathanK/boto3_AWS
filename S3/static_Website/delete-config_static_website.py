import boto3

s3 = boto3.client('s3')
response = s3.delete_bucket_website(Bucket='enter your valid bucket name')
print("bucket has been deleted",response)