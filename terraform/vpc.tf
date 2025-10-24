# Create a custom VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"      # Network range for your VPC
  tags = {
    Name = "Anjali-VPC"
  }
}

# Create a public subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"     # Subnet range inside the VPC
  map_public_ip_on_launch = true              # Auto-assign public IPs
  availability_zone       = "us-east-1a"      # Modify based on your region

  tags = {
    Name = "Public-Subnet"
  }
}

# Create a private subnet
resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.my_vpc.id
  cidr_block        = "10.0.2.0/24"           # Private range
  availability_zone = "us-east-1b"            # A different AZ

  tags = {
    Name = "Private-Subnet"
  }
}
