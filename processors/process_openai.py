import dotenv
import os
import streamlit as st
import uuid
from utils.pricing import calculate_cost_fixed
from utils.callLambda import invoke_lambda
from utils.getAzureOpenAIClient import get_openai_azure_core_client
from utils.getOpenAIClient import get_openai_core_client
from utils.extractFilePaths import extract_distinct_file_paths

from utils.format_source_paths import format_source_paths



   
def call_openai(user_name_logged, prompt, messages, model_name, max_output_tokens, temperature_value, kr_repos_chosen, domain_choice, similarity_search_output_documents):
    print ("In call_openai ")       
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key]
        
    OPENAI_CHOICE = os.getenv('OPENAI_CHOICE')    
    AZURE_OPENAI_VERSION= os.getenv('AZURE_OPENAI_VERSION')  
    
    if OPENAI_CHOICE == "Azure":
        deployment_name = model_name        
        client = get_openai_azure_core_client( AZURE_OPENAI_VERSION)
        openai_response = client.chat.completions.create(
            model=deployment_name, 
            messages=messages, 
            max_tokens=max_output_tokens,
            temperature = temperature_value
        )
    else:
        client = get_openai_core_client()
        openai_response = ""
        resp_container = st.empty()
        for delta in client.chat.completions.create(
                model=model_name ,
                messages=messages,
                stream=True,
        ):
            openai_response += (delta.choices[0].delta.content or "")
            resp_container.markdown(openai_response)
    
    # print (openai_response)
    message_content = openai_response
    if similarity_search_output_documents:
        distinct_file_paths, metadata_present = extract_distinct_file_paths(similarity_search_output_documents)
        print (distinct_file_paths)
        print (type (distinct_file_paths))
        resp_container.markdown (openai_response + "\n\n" + format_source_paths(distinct_file_paths))
    # Extracting input_tokens, output_tokens, and total_tokens
    input_tokens = 100
    output_tokens = 100
    total_tokens = 100
   
    cost  = calculate_cost_fixed (model_name, input_tokens, output_tokens)

    random_string = str(uuid.uuid4())
    promptId = "prompt-" + random_string     
        
    data = {    
        "userName": user_name_logged,
        "promptName": promptId,
        "prompt": prompt,
        "completion": message_content,
        "summary": "No Summary",
        "inputTokens": input_tokens,
        "outputTokens": output_tokens,
        "cost": cost,
        "feedback": "",
        "domain": domain_choice
    }

    # Invoke the Lambda function
    PROMPT_INSERT_LAMBDA = os.getenv('PROMPT_INSERT_LAMBDA')
    lambda_function_name = PROMPT_INSERT_LAMBDA
    lambda_response = invoke_lambda (lambda_function_name, data)
    if lambda_response != 200:
        raise Exception(f"AWS Lambda invocation failed with status code: {lambda_response['StatusCode']}")
    else:
        print ("Success calling lambda!")        
       
    return message_content, input_tokens, output_tokens, total_tokens, cost, promptId
