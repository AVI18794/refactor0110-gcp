import os
import dotenv 
from openai import OpenAI

def get_openai_azure_core_client( version):    
    print('get_openai_azure_core_client')
        
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
    
    from openai import AzureOpenAI
    
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version=version,
        azure_endpoint = os.getenv("AZURE_OPENAI_API_BASE")
    )   

    return client 