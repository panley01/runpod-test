FROM python:3.10-slim

WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy handler file
COPY src/handler.py /

# Start the container
CMD ["python3", "-u", "handler.py"]