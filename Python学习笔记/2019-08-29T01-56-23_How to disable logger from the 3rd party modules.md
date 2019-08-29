# How to disable logger from the 3rd party modules

Refer to: https://stackoverflow.com/questions/27538879/how-to-disable-loggers-from-other-modules

```py
logging.getLogger("elasticsearch").disabled = True

# Or
for mod in ("boto", "elasticsearch", "urllib3"):
    logging.getLogger(mod).disabled = True
```
