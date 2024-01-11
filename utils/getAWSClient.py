import os
import dotenv
import boto3
from ..config import config

def get_aws_client(service_name):    
    print('get_aws_client')
        
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
    aws_access_key_id = config.AWS_ACCESS_KEY_ID
    aws_secret_access_key = config.AWS_SECRET_ACCESS_KEY
    aws_region = config.AWS_DEFAULT_REGION
    aws_bucket = config.S3_BUCKET_NAME

    client = boto3.client(service_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    return client, aws_bucket
    
