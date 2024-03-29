import dotenv
import os
import streamlit as st
import uuid
from utils.pricing import calculate_cost_fixed
from utils.callLambda import invoke_lambda
from utils.getAzureOpenAIClient import get_openai_azure_core_client
from utils.getOpenAIClient import get_openai_core_client
from utils.extractFilePaths import extract_distinct_file_paths
import config as config
from utils.format_source_paths import format_source_paths


def call_openai(LLM_choice, user_name_logged, prompt, messages, model_name, max_output_tokens, temperature_value, kr_repos_chosen, domain_choice, similarity_search_output_documents):
    
    print ("In call_openai changed")   
    print (model_name)   
    print (max_output_tokens) 
    print (temperature_value)
    dotenv.load_dotenv(".env")
    env_vars = dotenv.dotenv_values()
    for key in env_vars:
        os.environ[key] = env_vars[key] 
    openai_response = ""
    resp_container = st.empty()
    if LLM_choice == "Azure":
        AZURE_OPENAI_VERSION= config.AZURE_OPENAI_VERSION
        deployment_name = model_name        
        client = get_openai_azure_core_client()
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature_value,
            max_tokens = max_output_tokens,
            stream=True
        )

        for chunk in response:
            if len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if delta.role:
                    print(delta.role + ": ", end="", flush=True)
                if delta.content:
                    print(delta.content, end="", flush=True)
                    openai_response += delta.content
                    resp_container.markdown(openai_response)
    else:
        client = get_openai_core_client()
        for delta in client.chat.completions.create(
                model=model_name ,
                messages=messages,
                temperature=temperature_value,
                max_tokens = max_output_tokens,
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
    PROMPT_INSERT_LAMBDA = config.PROMPT_INSERT_LAMBDA
    lambda_function_name = PROMPT_INSERT_LAMBDA
    (lambda_response_code, lambda_response) = invoke_lambda (lambda_function_name, data)
    if lambda_response_code != 200:
        raise Exception(f"AWS Lambda invocation failed with status code: {lambda_response['StatusCode']}")
    else:
        print ("Success calling lambda!")        
       
    return message_content, input_tokens, output_tokens, total_tokens, cost, promptId
