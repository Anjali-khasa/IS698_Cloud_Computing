# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "anjali-terraform-s3-demo"  
}

# Enable versioning for that bucket
resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.my_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}
