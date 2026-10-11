FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy configuration and environment files
COPY configs/ /app/configs/
COPY data/ /app/data/
COPY src/ /app/src/

# Install exact python dependencies
RUN pip install --no-cache-dir \
    numpy==1.24.3 \
    pandas==2.0.3 \
    scikit-learn==1.3.0 \
    statsmodels==0.14.0 \
    pyyaml==6.0.1

# Run benchmark script by default
CMD ["python", "src/benchmark.py"]
