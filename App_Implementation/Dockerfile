# Set base image (host OS)
FROM python:3.8-alpine
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
RUN apk add --no-cache gcc musl-dev linux-headers


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .
COPY nations.py .
COPY service service
COPY static static
COPY templates templates

# Specify the command to run on container start
CMD [ "python", "./app.py" ]