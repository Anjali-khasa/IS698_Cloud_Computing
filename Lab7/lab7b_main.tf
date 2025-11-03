
provider "aws" {
  region = "us-east-1"
}

variable "instances" {
  type = map(string)
  default = {
    "web1" = "t2.micro"
    "web2" = "t3.micro"
    "web3" = "t2.small"
  }
}

resource "aws_instance" "web" {
  for_each = var.instances

  ami           = "ami-***************"  
  instance_type = "t2.micro"
  subnet_id     = "subnet-*************"

  tags = {
    Name = each.key
  }
}
