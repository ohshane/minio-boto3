import boto3
from botocore.client import Config

# Initialize a session using MinIO.
s3 = boto3.resource(
    's3',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',
    config=Config(signature_version='s3v4'),
    endpoint_url='http://localhost:9000',
)

# Create a new bucket.
s3.create_bucket(Bucket='my-bucket')

# Upload a file to the bucket.
s3.Object('my-bucket', 'foo.txt').put(Body='Hello, world!')

# List all objects in a bucket.
for obj in s3.Bucket('my-bucket').objects.all():
    print(obj.key, obj.last_modified)
