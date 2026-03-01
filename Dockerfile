FROM python:3.10-slim

WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy handler file
COPY src/handler.py /

# Install model
RUN wget -q https://huggingface.co/black-forest-labs/flux.1-dev:3de623fc3c33e44ffbe2bad470d0f45bccf2eb21 -O /models/main.pt

# Start the container
CMD ["python3", "-u", "handler.py"]