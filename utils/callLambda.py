import os
import json
import boto3
import dotenv
import config as config

# Function to initialize environment variables from .env file
def load_env():
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]

# Function to invoke Lambda
def invoke_lambda(lambda_name, data):
    print ("In invoke_lambda")
    # load_env()

    # Retrieve AWS credentials and Lambda function name from environment variables
    aws_access_key_id = config.AWS_ACCESS_KEY_ID
    aws_secret_access_key = config.AWS_SECRET_ACCESS_KEY
    aws_region = config.AWS_DEFAULT_REGION

    # Initialize boto3 Lambda client
    lambda_client = boto3.client('lambda', aws_access_key_id=aws_access_key_id,
                                 aws_secret_access_key=aws_secret_access_key, 
                                 region_name=aws_region)

    # Invoke the Lambda function
    try:
        lambda_response = lambda_client.invoke(
            FunctionName=lambda_name,
            InvocationType='RequestResponse',  # Use 'Event' for asynchronous invocation
            Payload=json.dumps(data)
        )
    except Exception as e:
        return f"Error invoking Lambda: {str(e)}"

    # Check the response status code
    if lambda_response['StatusCode'] == 200:
        return 200
    else:
        raise Exception(f"AWS Lambda invocation failed with status code: {lambda_response['StatusCode']}")


