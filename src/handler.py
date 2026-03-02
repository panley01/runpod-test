import runpod
import torch
import os
import base64
from io import BytesIO
from diffusers import FluxPipeline

token = os.environ.get('HF_TOKEN')
model = "black-forest-labs/FLUX.1-dev"
if not token:
    raise ValueError('Please set your HF_TOKEN environment variable')

# Model is gated, auth is required for download due to licencing consent

print('Loading FLUX.1-dev')
pipe = FluxPipeline.from_pretrained(
    model,
    torch_dtype=torch.bfloat16,
    token=token,
    device_map = 'cuda',
)

# Define model outside of handler, to ensure this (heavy) process is not initiated on every call to the endpoint

def handler(event):
    print(f'Worker Start')
    input = event['input']
    
    prompt = input.get('prompt')

    print(f'Received prompt: {prompt}')

    image = pipe(
        prompt = prompt,
        height = input.get('height', 1024),
        width = input.get('width', 1024),
        max_sequence_length = 512
    ).images[0]

    buff = BytesIO()
    image.save(buff, format = 'JPEG')
    image_b64 = base64.b64encode(buff.getvalue()).decode('utf-8')
    image_string = f'data:image/jpeg;base64, {image_b64}'

    # Converting PIL Image to Base64 URI for easy display on frontend

    return {'image': image_string}

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler })