import os
import openai
import gradio
from dotenv import load_dotenv
load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")
userinput = input("Ask chatGPT a question: ")
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo', 
    messages= [{"role":"user","content":userinput}]
)
print(response)