import boto3 

website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

s3 = boto3.client('s3')
s3.put_bucket_website(Bucket='enter your bucket name',
                      WebsiteConfiguration=website_configuration)