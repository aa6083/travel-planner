#!/bin/bash
apt-get update -y
apt-get upgrade -y

apt-get install -y docker.io
systemctl start docker
systemctl enable docker

docker pull affanalrayyan/travel-planner:latest
docker run -d \
  -p 5000:5000 \
  -e GROQ_API_KEY=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 \
  --name travel-planner \
  --restart always \
  affanalrayyan/travel-planner:latest