# Work with S3 in Python

- boto3

```py
import boto3
s3 = boto3.resource(
    's3',
    aws_access_key_id = 'S3_ACCESS_KEY_ID',
    aws_secret_access_key = 'S3_SECRET_ACCESS_KEY',
#    endpoint_url = 'http://192.168.1.70:9000',
    endpoint_url = 's3://xxxx/',
)

obj = s3.Object('BUCKET_NAME', 'target_key')
data = obj.get()['Body'].read()
```
