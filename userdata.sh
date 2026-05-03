#!/bin/bash
apt-get update -y
apt-get upgrade -y

apt-get install -y docker.io
systemctl start docker
systemctl enable docker

docker pull affanalrayyan/travel-planner:latest
docker run -d \
  -p 5000:5000 \
  -e GROQ_API_KEY=your_groq_api_key_here \
  --name travel-planner \
  --restart always \
  affanalrayyan/travel-planner:latest