# Flask中的Global全局变量：g [DRAFT]

- How to use
- Doesn't work in thread, subprocess and gevent
- `copy_current_request_context` doesn't work in thread as well
- Inside gevent worker, the request context is lost


## How to use

```py
from flask import Flask, g as flask_g

app = Flask(__name__)

@app.route('/hello')
def hello():
    flask_g.glo = 'not set'
    f()
    data = getattr(flask_g, 'glo')
    print(data)
    return ''

def f():
    flask_g.glo = 'changed'

app.test_client().get('/hello', headers={'myhead': 'not set'})
```
The result is `changed`.
This `f()` has to be in the request context.


## Lose context inside Gevent worker

```py
import gevent
from flask import Flask, has_request_context

app = Flask(__name__)

@app.route('/hello')
def hello():
    gevent.joinall([gevent.spawn(has_context)])
    return ''

def has_context():
    print('Has context:', has_request_context())

resp = app.test_client().get('/hello', headers={'myhead': 'not set'})
```
The result is `False`. Same thing goes with `Thread` and `Process`.
