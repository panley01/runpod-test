FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

WORKDIR /

# Install dependencies
RUN apt-get update && apt-get install -y python3.11 python3-pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy handler file
COPY src/handler.py /

# Start the container
CMD ["python3", "-u", "handler.py"]