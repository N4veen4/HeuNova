# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies for OpenCV and other tools
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Create a non-root user for security (Hugging Face Spaces requirement)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Create the static and models directory
RUN mkdir -p $HOME/app/static $HOME/app/models

# Set working directory to app
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app
# Use --chown to ensure the files belong to the non-root user
COPY --chown=user . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application
# Using port 7860 as it's the default for Hugging Face Spaces
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
