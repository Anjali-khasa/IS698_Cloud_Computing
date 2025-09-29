import boto3

s3 = boto3.client('s3')
bucket_name = 'anj95-boto3-s3-bucket-lab3'

s3.delete_bucket(Bucket=bucket_name)
print(f'Bucket {bucket_name} deleted successfully!')
