import boto3
import logging
from botocore.exceptions import ClientError
import os

def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    
    s3 = boto3.client('s3')
    try:
        response = s3.upload_file(file_name,bucket,object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#for object uploading use 
#s3 = boto3.client('s3')
#with open("FILE_NAME","rb") as f: # rb mean readable file
#   s3.upload_fileobj(f,"BUCKET_NAME","OBJECT_NAME")
        