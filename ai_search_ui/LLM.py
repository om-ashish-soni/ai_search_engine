import os
from dotenv import load_dotenv


# formatting prompt
# def format_prompt_1(Query,Context):
#   prompt=f"""
#   Answer the query in detail 
#   Format as (Source Number) (Source Url) ([Answer Retrived by you from Current Source ])
#   "{Query}" from the Web Results below :
#   Web Results : {Context}
#   """
#   return prompt

def format_prompt_1(Query,Context):
    prompt = f"""
    Assume you are a search engine ,
     
    Answer the query in detail "{Query}" from the Context Provided below :

    Context : {Context}
    """
    
    return prompt


 
# loading env varaibles
load_dotenv()
# REPLACE WITH YOUR HUGGING FACE ACCOUNT TOKEN ( Go to settings and get access token from hugging face)
hf_token=os.getenv('HF_TOKEN')

# querying
def query(payload):
    
    import requests

    # Replace API URL with your LLM API URL ( from hugging face. i.e. )
    # for example HF_LLM_INFERENCE_CHECKPOINT='https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'
    # API_URL='https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'
    API_URL="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    # API_URL = os.getenv('HF_LLM_INFERENCE_CHECKPOINT')

    headers = {"Authorization": "Bearer "+hf_token}
    
    # retriving response
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def prompt_format_2(Query,Context,PreviousAnswer=None):
  formatted_prompt=format_prompt_1(Query,Context)
  prompt='<s>[INST] '+formatted_prompt+'\n [/INST] Model answer</s>'
  return prompt

def infer(Query,Context,PreviousAnswer=None):
  try:
      print("going to infer")

      prompt=prompt_format_2(Query,Context,PreviousAnswer)
      
      # print("generated prompt",prompt)
      output = query({
          "inputs": prompt,
          "parameters": 
        {
          "contentType": "application/json",
          "max_tokens": 20400,
          "max_new_tokens": 4000,
          "return_full_text": False
        }
      })

      return output[0]['generated_text']
  except Exception as e:
        print(f"An error occurred: {e}")
        return f"could not generate answer Due to Error, please try after some time ,{e} "  