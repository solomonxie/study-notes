# Unit test

## Unit test on Exceptions

```py
import unittest

class MyException(Exception):
    pass

def some_problematic_function():
    raise MyException('[ERR] Shit happens.')

class TestMe(unittest.TestCase):
    def test_something(self):
        self.assertIsNone(None, None)
        with self.assertRaises(MyException) as cm:
            some_problematic_function()
        print(str(cm.exception))


if __name__ == '__main__':
    unittest.main()
```


With mock to test exception:
```py
import unittest
from unittest import TestCase, mock

class MyError(Exception):
    code = 500
    description = "Internal Server Error"

def some_problematic_function(s):
    raise MyError(s)

def get_exception(s):
    return MyError(s)

class TestMe(TestCase):

    def test_something(self):
        self.assertIsNone(None, None)
        with self.assertRaises(MyError) as cm:
            some_problematic_function('[ERR] Shit happens.')
        print(str(cm.exception))

    def test_raises(self):
        ex = get_exception('[ERR] Shitty happened.')
        type(ex).query = mock.PropertyMock(side_effect=MyError)
        with self.assertRaises(MyError) as ct:
            ex.query()
        self.assertEqual(500, ct.exception.code)
        self.assertEqual("Internal Server Error", ct.exception.description)

if __name__ == '__main__':
    unittest.main()
```
