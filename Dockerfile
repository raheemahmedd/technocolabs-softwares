# Use the official Python image as the base image
#FROM python:3
#FROM python:3.8-slim-buster


# Update the package manager and install python3-pip
# The error message suggests that the package manager is not updated and python3-pip is missing, so we need to update the package manager and install python.
3RUN apt-pip-get update \
    && apt-get install -y python3-pip

# Create the working directory in the container
#WORKDIR /app

# Copy the application files into the working directory
#COPY . /app

# Install the application dependencies
# fixed typo changed: "pip3" to "python3-pip"
# The error message states that python3-pip is missing, so it needs to be installed.
#RUN python3 -m pip install -r requirements.txt

# Define the entry point for the container
#CMD ["python", "app.py"]
#FROM python:3-alpine3.15
#WORKDIR /app
#COPY . /app
#RUN pip install -r requirements.txt
#EXPOSE 3000
#CMD python ./index.py
FROM python:3.10

RUN apt-get update && apt-get install -y --allow-unauthenticated universe

RUN apt-get install python3-pip

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
