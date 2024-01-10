import dotenv
import pinecone
import os
from config import config

def get_pinecone_index():
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
    pinecone.init (
        api_key = config.PINECONE_API_KEY,
        environment = config.PINECONE_ENVIRONMENT  
    )
    pinecone_index_name = config.PINECONE_INDEX_NAME
    
    index = pinecone.Index(pinecone_index_name)
    return index