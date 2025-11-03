terraform {
  backend "s3" {
    bucket         = "terraform-state-anjalikhasa-lab7a"   
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}

provider "aws" {
  region = "us-east-1"
}


resource "aws_instance" "my_ec2" {
  ami           = "ami-***************"   
  instance_type = "t2.micro"
  key_name      = "anj-SSH-key-pair"  
  subnet_id     = "subnet-***************"      
  tags = {
    Name = "Anjali-Terraform-EC2-Instance"         
  }
}

