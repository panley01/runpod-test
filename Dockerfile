FROM python:3.10-slim

WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy handler file
COPY src/handler.py /

# Install model
RUN python -c "from diffusers import AutoModel; AutoModel.from_pretrained('black-forest-labs/FLUX.1-dev')"

# Start the container
CMD ["python3", "-u", "handler.py"]