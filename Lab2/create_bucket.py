import boto3

s3 = boto3.client('s3')
bucket_name = 'anj95-boto3-s3-bucket-lab3' 

response = s3.create_bucket(Bucket=bucket_name)
print(f'Bucket {bucket_name} created successfully!')
