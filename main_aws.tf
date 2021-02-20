terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "BlueLion" {
  ami           = "ami-0245ae71716af2644"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_nametag
  }
}

