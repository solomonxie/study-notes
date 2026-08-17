# Python Mock Collection [DRAFT]

What is a mock?


Why do we need mock?



## Mocking Principle



## Mocking Tricks & Tips



## Built-in Mock Utilities

Library: `unittest.mock`

Common mocks:
- Method mock
- Class property mock
- Importation mock

Common mock terms:
- Patch
- MagicMock
- Return value
- Side effect
- New Callable


Mock a property of class:
```py
from unittest.mock import patch

class A:
    a = 0

with patch.object(A, 'a', 9):
    print(A.a)
# [OUT] 9
```

Mock a method of an instance:
```py
from unittest.mock import patch, MagicMock
# directly return result
>>> class A: pass
>>> a = A()
>>> a.func = MagicMock(return_value=7)
>>> a.func()
7

# return error
>>> a.func = MagicMock(side_effect=KeyError('I am an exception')))
>>> a.func()
KeyError: 'I am an exception'
```

Mock a method from a module:
```py
#a.py
def target(n):
    return n

#b.py
from a import target

@patch('a.target')
def main(mock_target):
    mock_target.new = lambda x: x*2
    target(3)
```


## DB Mock (Relational DB)


## Redis Mock

Library: `Fakeredis`

```py
redis_conn = fakeredis.FakeStrictRedis()

# Proper use
class TestRedisutils(TestCase):
    def setUp(self):
        self.redis_conn = FakeRedis()

    def tearDown(self):
        self.redis_conn.flushall()
```


## S3 Mock

Library: `MinIO`

```sh
mkdir -p ~/workspace/dataset/fake-s3
cd ~/workspace/dataset/fake-s3
wget https://dl.minio.io/server/minio/release/darwin-amd64/minio
chmod +x minio
mkdir data

# Run on foreground
./minio server ./data
```

**Work with MinIO CLI client:**
```sh
# Install client `mc`
$ brew install mc

# Add S3 Server (according to the local server setting)
$ mc config host add MyS3 http://192.168.1.51 BKIKJAA5BMMU2RHO6IBB V7f1CwQqAcwo80UEIJEjc5gVQUSSx5ohQ9GSrr12

# List
$ mc ls MyS3/BucketName/path/to/destination --recursive

# Remove a directory
$ mc rm --force --recursive MyS3/BucketName/path/to/destination
Refer to: https://docs.min.io/docs/minio-client-quickstart-guide.html
```

Test if the MinIO at host machine can be discovered inside of docker container:
```sh
# In docker container, try to connect with Host IP address:
$ telnet 192.168.2.238 9000
```


Host IP not found error:
It's because of the IP address inside the container is random assigned.

Debugging:
```sh
# Host IP address:
# --> 192.168.2.238

# Inside the container (run multiple times):
$ ifconfig
inet 172.19.0.4  netmask 255.255.0.0  broadcast 172.19.255.255   # OK
inet 172.21.0.4  netmask 255.255.0.0  broadcast 172.21.255.255   # OK

# `Docker.app` Preference setting -> `Docker subnet`:
# --> 192.168.65.0/24
# Change to:
# --> 192.168.2.0/24

$ ifconfig
inet 172.18.0.4  netmask 255.255.0.0  broadcast 172.21.255.255   # FAILED TO CONNECT HOST
inet 172.19.0.4  netmask 255.255.0.0  broadcast 172.19.255.255   # FAILED TO CONNECT HOST
```

Solution (temp): https://forums.docker.com/t/accessing-host-machine-from-within-docker-container/14248/5

```sh
$ docker network mynet create -d bridge --subnet 192.168.0.0/24 --gateway 192.168.0.1
$ docker network ls                                                                                                                                                                   
NETWORK ID          NAME                      DRIVER              SCOPE
3f65f512b9cb        aa-bulk-grabber_default   bridge              local
a5fc91acb740        mynet                     bridge              local

# docker-compose.yml
services:
    aa-bulk-grabber-run:
        networks:
            - mynet
            - aa-bulk-grabber_default
networks:
    mynet:
        external: true
    aa-bulk-grabber_default:
        external: true
```



## Http Mock

Library: `Mocket`

Refer to: https://pypi.org/project/mocket/

Mock a GET request/response:
```py
import requests
from mocket import Mocket
from mocket.mockhttp import Entry
url = 'https://baidu.com'
Entry.single_register('GET', url, status=200, body='hallo', headers={'ua': 'haha'})
Mocket.enable()
cnt = requests.get(url).content
print(cnt)
# 'hallo'
```


Mock a POST request/response:
```py
import requests
from mocket import Mocket
from mocket.mockhttp import Entry

url, mock_data, mock_headers = 'http://baidu.com', '{"name": "foo"}', {'head': 'sth'}
Entry.single_register('POST', url, status=200, body=mock_data, headers=mock_headers)
Mocket.enable()

resp = requests.post(url, headers={'any': 'any'}, data='any post body')
print(resp.content)
print(resp.headers)
print(resp.status_code)
```

The `Mocket` will add extra headers in the response, like:
```
{'Status': '300', 'Date': 'Fri, 14 Feb 2020 07:23:47 GMT', 'Server': 'Python/Mocket', 'Connection': 'clo
se', 'Content-length': '15', 'Content-type': 'text/plain; charset=utf-8', 'Head': 'sth'}
```

If we don't want it to add extra headers, we have to rewrite the response class:
```py
import requests
from mocket import Mocket
from mocket.mockhttp import Entry, Response


class Res(Response):
    def set_extra_headers(self, headers):
        self.headers = headers

    def set_base_headers(self):
        pass


url, mock_data, mock_headers = 'http://baidu.com', '{"name": "foo"}', {'head': 'sth'}
Entry.register('POST', url, Res(body=mock_data, status=300, headers=mock_headers))
Mocket.enable()

resp = requests.post(url, headers={'any': 'any'}, data='any post body')
print(resp.content)
print(resp.headers)
print(resp.status_code)
```

> But Mocket is very limited on the mock requests. It can't recognize POST requests with different body, and can't let you customize the response content (unless you rewrite its method).

**A better alternative library: `pook`**

Refer to: https://pook.readthedocs.io/en/latest/examples.html

Mock on POST, returns with different response based on different request body/headers:
```py
import json
import requests

import pook

pook.on()

# Register a POST mock
(pook.post('httpbin.org/post')
    .json({'foo': 'bar'})
    .type('json')
    .header('Client', 'requests')
    .reply(204)
    .headers({'server': 'pook'})
    .json({'body': 'FIRST'}))
# Register with same URL but diff BODY
(pook.post('httpbin.org/post')
    .json({'foo': 'ha'})
    .type('json')
    .header('Client', 'requests')
    .reply(204)
    .headers({'server': 'pook'})
    .json({'body': 'SECOND'}))

res = requests.post(
    'http://httpbin.org/post',
    data=json.dumps({'foo': 'bar'}),
    headers={'Client': 'requests', 'Content-Type': 'application/json'}
)
print(res.status_code)
print(res.headers)
print(res.content)

res = requests.post(
    'http://httpbin.org/post',
    data=json.dumps({'foo': 'ha'}),
    headers={'Client': 'requests', 'Content-Type': 'application/json'}
)
print(res.status_code)
print(res.headers)
print(res.content)

pook.off()
```
