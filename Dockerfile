# Use a PyTorch image with CUDA 11.8 as the base
FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-runtime

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python 3.11.3 (optional if you require an exact version and it's different from the base image)
# RUN apt-get update && apt-get install -y python3.11

# Install necessary libraries
RUN pip install opencv-python-headless \
    einops \
    imageio \
    gradio==4.27.0 \
    pillow==10.3.0

# Expose port for the web GUI
EXPOSE 7860

# Command to run upon container startup.
CMD ["python", "app.py"]