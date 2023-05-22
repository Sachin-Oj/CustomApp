FROM python:3-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY . /app

RUN pip install -r requirement.txt

EXPOSE 5000
CMD python ./server.py