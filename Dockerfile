# Use the official nginx image as a base
FROM python:3.13.6-slim-bookworm

# Temporary for debugging
# Install openssh for SSH capabilities
# RUN apt install openssh-server
RUN apt-get update && apt-get install -y openssh-server 


