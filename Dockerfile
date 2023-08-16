
# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
# Fixed typo changed: "requeriments.txt" to "requirements.txt"
# The error message states that the requirements.txt file is missing, so it needs to be present in the same directory as the Dockerfile.
# Install python3-pip using apt-get
RUN apt-get update && apt-get install -y python3-pip
# Install the application dependencies from requirements.txt
# Fixed typo changed: "pip3 install.txt" to "pip3 install -r requirements.txt"
# The correct syntax to install packages from a requirements.txt file is "pip3 install -r requirements.txt"
RUN pip3 install -r requirements.txt


CMD ["flask", "run", "--host=0.0.0.0"]
