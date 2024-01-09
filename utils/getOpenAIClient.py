import os
import dotenv
from openai import OpenAI  
def get_openai_core_client():    
    print('call_openai_core')
      
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
        
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_ORGANIZATION = os.getenv('OPENAI_ORGANIZATION')
    client = OpenAI(organization = OPENAI_ORGANIZATION, api_key = OPENAI_API_KEY)

    return client 