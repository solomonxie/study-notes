# Django Middleware [DRAFT]

> "The Middlware classes **are called twice** during the `Request/Response Life Cycle`. For that reason, the `order` you define the Middlwares in the MIDDLEWARE_CLASSES configuration is important."

[Refer to: How to Create a Custom Django Middleware](https://simpleisbetterthancomplex.com/tutorial/2016/07/18/how-to-create-a-custom-django-middleware.html)


Django built-in middlewares (installed by default):
```py
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
