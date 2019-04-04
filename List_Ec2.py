import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
#print("Bucket List: %s" % buckets)



client = boto3.client('ec2')

custom_filter = [{
    'Name':'tag:Owner', 
    'Values': ['GSA']}]

response = client.describe_instances(Filters=custom_filter)
##print(response)

iam = boto3.client('iam')

# Create user
response = iam.create_user(UserName='Valaxy-User-01')

# print(response)

paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)


iam.delete_user(UserName='Valaxy-User-01')