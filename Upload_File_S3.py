import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'List_S3_Bucket.py'
bucket_name = 'my-india-201811'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)