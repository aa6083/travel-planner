#!/bin/bash
yum update -y
yum install -y docker
service docker start
docker pull affanalrayyan/travel-planner:latest
docker run -d -p 5000:5000 -e OPENAI_API_KEY="" affanalrayyan/travel-planner:latest