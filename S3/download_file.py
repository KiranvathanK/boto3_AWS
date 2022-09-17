import boto3

s3 = boto3.client('s3')
response = s3.download_file('BUCKET_NAME','OBJECT_NAME','FILE_NAME')
print('downloded file is',response)


#downlaod file as object download_fileobj
# s3 = boto3.client('s3)
#with open('FILE_NAME','wb')as f: #wb mean writeable file
# s3.download_fileobj('BUCKET_NAME','OBJECT_NAME',f)