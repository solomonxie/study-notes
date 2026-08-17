# Procfile: Deploy as Code (Continuous Delivery) [DRAFT]

[Refer to: The Procfile - Heroku Dev Center](https://devcenter.heroku.com/articles/procfile)

A `Procfile` is a file remembers that the _commands_ you usually type by hands to deploy your web application like Django, Flask and such WebApp projects.
It's indeed the file to implement the concept `Deploy as code` that tracks the important deployment commands.

A `Procfile` can look like this:
```Procfile
web: gunicorn -b "0.0.0.0:$PORT" -w 4 myapp:app
worker: python worker.py --priority high,med,low
worker_low: python worker.py --priority med,low
```

And with the Procfile management tool `Honcho`, all you need to do to start a service is to type:
```sh
$ honcho start
```

## Honcho: manage Procfile-based applications
`A python clone of Foreman. For managing Procfile-based applications`

Refer to: https://honcho.readthedocs.io/en/latest/
Refer to: https://github.com/nickstenning/honcho

Install `Honcho`:
```sh
$ pip install honcho
```
