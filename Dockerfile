FROM python:3.11-slim

WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install ultralytics
RUN pip install fastapi uvicorn


# Install NVIDIA CUDA toolkit for GPU support (optional)
# This requires having an NVIDIA GPU and Docker with GPU support installed

#RUN pip install nvidia-pyindex
#RUN pip install nvidia-tensorflow[all]  # For TensorFlow GPU
#RUN pip install torch torchvision torchaudio  # For PyTorch GPU

# Expose port 8000 for FastAPI app
EXPOSE 8000

# Command to run the FastAPI app CMD
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
