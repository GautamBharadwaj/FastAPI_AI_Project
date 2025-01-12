FROM python:3.11-slim

WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install ultralytics
RUN pip install fastapi uvicorn
RUN pip install python-multipart

# Expose port 8000 for FastAPI app
EXPOSE 8000

# Command to run the FastAPI app CMD
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
