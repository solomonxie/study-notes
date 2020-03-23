# Boto3操作腾讯云COS对象存储 (兼容S3)

```py
import boto3

client = boto3.client(
    's3',
    region_name='ap-beijing',
    aws_access_key_id='access_key',
    aws_secret_access_key='secret_key',
    endpoint_url='https://cos.ap-guangzhou.myqcloud.com'
)

print(client.list_buckets())
```
