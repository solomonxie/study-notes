# How to Mock S3 with Boto3 & MinIO (Entire test framework)


Docker-compose:

```yaml
version: '3.7'

services:
  myapp:
    image: myname/myapp:latest
    links:
      - s3-minio
    volumes:
      - ./:/src

  s3-minio:
    image: registry.hub.docker.com/minio/minio:latest
    env_file:
     - ./envfile-local.txt
    volumes:
      - /tmp/:/data
    command: minio server /data

```

Environment variables for MinIO:

```txt
#envfile-local.txt
# MinIO for testing S3
MINIO_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
MINIO_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```



Boto3 operation with S3/MinIO and boto3:

```py
import os
import boto3
from logging import getLogger

import settings

logger = getLogger(__name__)


class S3Operator:
    def __init__(self, access_key=None, secret=None, endpoint=None, region=None):
        self.client = self.get_s3_client(
            access_key or settings.AWS_ACCESS_KEY_ID,
            secret or settings.AWS_SECRET_ACCESS_KEY,
            endpoint=endpoint,
            region=region
        )
        self.resource = self.get_s3_resource(
            access_key or settings.AWS_ACCESS_KEY_ID,
            secret or settings.AWS_SECRET_ACCESS_KEY,
            endpoint=endpoint,
            region=region
        )

    def get_s3_client(self, access_key, secret, endpoint=None, region=None):
        return boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret,
            endpoint_url=endpoint,
            region_name=region,
            # config=boto3.session.Config(signature_version='s3v4'),
        )

    def get_s3_resource(self, access_key, secret, endpoint=None, region=None):
        return boto3.resource(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret,
            endpoint_url=endpoint,
            region_name=region,
            # config=boto3.session.Config(signature_version='s3v4'),
        )

    def upload_file(self, localpath, bucket_name, object_name=None):
        if not os.path.exists(localpath):
            return False
        object_name = object_name or os.path.basename(localpath)
        try:
            self.client.upload_file(localpath, bucket_name, object_name)
        except S3Exception as ex:
            print(ex)
        return True

    def download_file_blob(self, bucket_name, object_name):
        obj = self.resource.Object(bucket_name, object_name)
        body = obj.get()
        blob = body['Body'].read()
        return blob

    def upload_file_blob(self, file_blob, bucket_name, object_name):
        try:
            self.client.put_object(Bucket=bucket_name, Key=object_name, Body=file_blob)
        except S3Exception as ex:
            print(ex)
        return True

    def get_signed_url(self, bucket_name, object_name, expiredin=86400, httpmethod=None):
        url = self.client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name,
            },
            ExpiresIn=expiredin,
            HttpMethod=httpmethod,
        )
        return url

    def create_bucket_if_not_exists(self, bucket_name):
        existing = [b['Name'] for b in self.client.list_buckets()['Buckets']]
        if bucket_name not in existing:
            info = self.resource.create_bucket(Bucket=bucket_name)
            print('Created bucket:', info)
        return self.resource.Bucket(bucket_name).creation_date

    def delete_bucket(self, bucket_name):
        existing = [b['Name'] for b in self.client.list_buckets()['Buckets']]
        if bucket_name in existing:
            bucket = self.resource.Bucket(bucket_name)
            _ = [key.delete() for key in bucket.objects.all()]
            bucket.delete()

    def list_objects(self, bucket_name):
        keys = [obj.key for obj in self.resource.Bucket(bucket_name).objects.all()]
        return keys
```



Test cases for S3/MinIO:

```py
import urllib
from unittest import TestCase

import S3Operator


class TestS3(TestCase):
    def setUp(self):
        # Set the configs according to the "envfile-local.txt"
        self.s3 = S3Operator(
            access_key='AKIAIOSFODNN7EXAMPLE',
            secret='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
            endpoint='http://s3-minio:9000'
        )
        self.bucket_name = 'fakebucket'
        self.s3.delete_bucket(self.bucket_name)
        self.s3.create_bucket_if_not_exists(self.bucket_name)

    def tearDown(self):
        self.s3.delete_bucket(self.bucket_name)

    def test_upload(self):
        result = self.s3.upload_file('./README.md', self.bucket_name, 'README.md')
        self.assertTrue(result)
        objects = self.s3.list_objects(self.bucket_name)
        self.assertEqual(1, len(objects))
        self.assertIn('README.md', objects)

    def test_download(self):
        result = self.s3.upload_file_blob('[1, 2]', self.bucket_name, 'nums.json')
        blob = self.s3.download_file_blob(self.bucket_name, 'nums.json')
        self.assertEqual('[1, 2]', blob)

    def test_signed_url(self):
        self.s3.upload_file('./README.md', self.bucket_name, 'README.md')
        url = self.s3.get_signed_url(self.bucket_name, 'README.md')
        urlobj = urllib.parse.urlparse(url)
        self.assertEqual(f'/{self.bucket_name}/README.md', urlobj.path)
        params = urllib.parse.parse_qs(urlobj.query)
        self.assertListEqual(['AWSAccessKeyId', 'Signature', 'Expires'], list(params.keys()))
        self.assertEqual(['AKIAIOSFODNN7EXAMPLE'], params['AWSAccessKeyId'])
```


