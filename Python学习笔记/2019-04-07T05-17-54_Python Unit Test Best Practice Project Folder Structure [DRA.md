# Python Unit Test Best Practice: Project Folder Structure [DRAFT]


## Simplest

```
myproject
├── dosomething.py
└── test_dosomething.py
```

and what's in `test_dosomething.py` is:
```py
# myproject/test_dosomething.py

import unittest
import dosomething

# .......
```


## Best Practice

```
myproject
├── application
│   ├── __init__.py
│   └── dosomething.py
└── tests
    ├── __init__.py
    └── test_dosomething.py
```

How to run tests?
```sh
cd myproject
pytest -sv tests/
# or
python -m unittest tests.test_dosomethin
```

Notice that all `__init__.py` are empty files.
And the tricky part is always at `importation` part of `test_xxxx.py`:
```py
# myproject/tests/test_dosomething.py

import unittest
from application.dosomething import hello

# .......
```
