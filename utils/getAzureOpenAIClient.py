import os
import dotenv 
from openai import OpenAI
import config as config

def get_openai_azure_core_client():    
    print('get_openai_azure_core_client')
        
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
    
    from openai import AzureOpenAI
    
    client = AzureOpenAI(
        api_key=config.AZURE_OPENAI_API_KEY,  
        api_version=config.AZURE_OPENAI_VERSION,
        azure_endpoint = config.AZURE_OPENAI_ENDPOINT
    )   

    return client 