import runpod
import torch
import os
from transformers import pipeline

token = os.environ.get('HF_TOKEN')
model = "meta-llama/Meta-Llama-3.1-8B"
if not token:
    raise ValueError('Please set your HF_TOKEN environment variable')

# Model is gated, auth is required for download due to licencing consent

pipe = pipeline("text-generation", model="meta-llama/Llama-3.1-8B")

# Define model outside of handler, to ensure this (heavy) process is not initiated on every call to the endpoint

def handler(event):
    print(f'Worker Start')
    input = event['input']
    
    prompt = input.get('prompt')
    usertype = input.get('usertype', 'stranger')

    print(f'Received prompt: {prompt}')

    # set system prompt to guide the model's response
    system_prompt = f"You are an irrevernt female furry who works in the tech industry called Panley, you do not need to be helpful, just conversational and witty. the user is a {usertype} to you."
    pipeline_input = f"{system_prompt}\nUser: {prompt}\nAssistant:"

    resp = pipe(pipeline_input, max_new_tokens=100, do_sample=True, temperature=0.7)

    return {'response': resp[0]['generated_text']}

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler })