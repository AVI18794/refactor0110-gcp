from google.cloud import secretmanager
import ast
import os

def access_secret_version(secret_id, version_id="latest"):
    project_id = os.environ.get("PROJECT_ID")
    if project_id is None:
        raise ValueError("Enviornment variable 'PROJECT_ID' IS NOT SET.")
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}" 
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

workbench_secret_key = 'workbench0110'
config_string= str(access_secret_version(workbench_secret_key))
config= ast.literal_eval(config_string)


# CREDENTIALS

OPENAI_CHOICE = config['OPENAI_CHOICE']
OPENAI_API_KEY = config['OPENAI_API_KEY']
AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']
AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
AWS_DEFAULT_REGION = config['AWS_DEFAULT_REGION']
S3_BUCKET_NAME = config['S3_BUCKET_NAME']
S3_BUCKET_PATH = config['S3_BUCKET_PATH']
PINECONE_INDEX_NAME = config['PINECONE_INDEX_NAME']
S3_BUCKET_INPUT_PATH = config['S3_BUCKET_INPUT_PATH']
PINECONE_API_KEY = config['PINECONE_API_KEY']
PINECONE_ENVIRONMENT = config['PINECONE_ENVIRONMENT']
SERPAPI_API_KEY = config['SERPAPI_API_KEY']
HUGGINGFACEHUB_API_TOKEN = config['HUGGINGFACEHUB_API_TOKEN']
BING_SUBSCRIPTION_KEY = config['BING_SUBSCRIPTION_KEY']
BING_SEARCH_URL = config['BING_SEARCH_URL']
BARD_API = config['BARD_API']
BARD_API_OLD = config['BARD_API_OLD']
STATIC_ASSEST_BUCKET_URL = config['STATIC_ASSEST_BUCKET_URL']
STATIC_ASSEST_BUCKET_FOLDER = config['STATIC_ASSEST_BUCKET_FOLDER']
LOGO_NAME = config['LOGO_NAME']
PROMPT_INSERT_LAMBDA = config['PROMPT_INSERT_LAMBDA']
PROMPT_QUERY_LAMBDA = config['PROMPT_QUERY_LAMBDA']
PROMPT_UPDATE_LAMBDA = config['PROMPT_UPDATE_LAMBDA']
S3_PUBLIC_ACCESS = config['S3_PUBLIC_ACCESS']
S3_PUBLIC_ACCESS_PATH = config['S3_PUBLIC_ACCESS_PATH']
OPENAI_ORGANIZATION = config['OPENAI_ORGANIZATION']
UPDATE_CONFIG_LAMBDA = config['UPDATE_CONFIG_LAMBDA']
QUERY_CONFIG_LAMBDA = config['QUERY_CONFIG_LAMBDA']
SNOWFLAKE_USER = config['SNOWFLAKE_USER']
SNOWFLAKE_PASSWORD = config['SNOWFLAKE_PASSWORD']
SNOWFLAKE_ACCOUNT = config['SNOWFLAKE_ACCOUNT']
SNOWFLAKE_WAREHOUSE = config['SNOWFLAKE_WAREHOUSE']
SNOWFLAKE_ROLE = config['SNOWFLAKE_ROLE']
SNOWFLAKE_DATABASE = config['SNOWFLAKE_DATABASE']
SNOWFLAKE_SCHEMA = config['SNOWFLAKE_SCHEMA']
SCHEMA_PATH = config['SCHEMA_PATH']
SNOWBENCH_URL = config['SNOWBENCH_URL']
AZURE_OPENAI_API_KEY = config['AZURE_OPENAI_API_KEY']
AZURE_OPENAI_API_TYPE = config['AZURE_OPENAI_API_TYPE']
AZURE_OPENAI_ENDPOINT = config['AZURE_OPENAI_ENDPOINT']
AZURE_OPENAI_GPT432K = config['AZURE_OPENAI_GPT432K']
AZURE_OPENAI_API_VERSION_GPT432K = config['AZURE_OPENAI_API_VERSION_GPT432K']
AZURE_OPENAI_GPT4 = config['AZURE_OPENAI_GPT4']
AZURE_OPENAI_API_VERSION_GPT4 = config['AZURE_OPENAI_API_VERSION_GPT4']
AZURE_OPENAI_GPT35TURBO16K = config['AZURE_OPENAI_GPT35TURBO16K']
AZURE_OPENAI_API_VERSION_GPT35TURBO16K = config['AZURE_OPENAI_API_VERSION_GPT35TURBO16K']
AZURE_OPENAI_GPT35TURBO = config['AZURE_OPENAI_GPT35TURBO']
AZURE_OPENAI_API_VERSION_GPT35TURBO = config['AZURE_OPENAI_API_VERSION_GPT35TURBO']
AZURE_OPENAI_VERSION = config['AZURE_OPENAI_VERSION']
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = config['AZURE_OPENAI_EMBEDDING_DEPLOYMENT']
