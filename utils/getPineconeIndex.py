import dotenv
import pinecone
import os

def get_pinecone_index():
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
    pinecone.init (
        api_key = os.getenv('PINECONE_API_KEY'),
        environment = os.getenv('PINECONE_ENVIRONMENT')   
    )
    pinecone_index_name = os.getenv('PINECONE_INDEX_NAME')
    
    index = pinecone.Index(pinecone_index_name)
    return index