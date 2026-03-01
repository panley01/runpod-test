import runpod
import torch
import os
import base64
from io import BytesIO
from diffusers import FluxPipeline

token = os.environ.get('HF_TOKEN')
model = os.environ.get('MODEL')
if not token:
    raise ValueError('Please set your HF_TOKEN environment variable')

print('Loading FLUX.1-dev')
pipe = FluxPipeline.from_pretrained(
    model,
    torch_dtype=torch.bfloat16,
    token=token
)

pipe.enable_model_cpu_offload()

def handler(event):
    print(f'Worker Start')
    input = event['input']
    
    prompt = input.get('prompt')

    print(f'Received prompt: {prompt}')

    image = pipe(
        prompt = prompt,
        height=input.get('height', 1024),
        width=input.get('width', 1024),
        max_sequence_length=512
    ).images[0]

    buff = BytesIO()
    image.save(buff, format='png')
    image_string = base64.b64encode(buff.getvalue()).decode('utf-8')

    return {image: image_string}

# Start the Serverless function when the script is run
if __name__ == '__main__':
    runpod.serverless.start({'handler': handler })