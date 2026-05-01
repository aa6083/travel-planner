Set-Content C:\travel-planner\terraform\main.tf @'
provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "travel_sg" {
  name = "travel-planner-sg"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "travel_app" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.travel_sg.id]
  user_data              = <<-EOF
#!/bin/bash
yum update -y
yum install -y docker
service docker start
docker pull affanalrayyan/travel-planner:latest
docker run -d -p 5000:5000 affanalrayyan/travel-planner:latest
EOF

  tags = {
    Name = "Travel-Planner"
  }
}
'@