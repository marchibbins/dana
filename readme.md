# Dana

A simple [Twelve-Factor](http://www.12factor.net/) Django application.

### Dependencies

- [Django](https://www.djangoproject.com/) - Python Web framework
- [Gunicorn](http://gunicorn.org/) - WSGI HTTP server
- [Honcho](https://github.com/nickstenning/honcho) - a Python clone of [Foreman](http://ddollar.github.com/foreman/)

### Getting started

1. Install requirements (use [virtualenv](https://pypi.python.org/pypi/virtualenv))

        $ pip install -r requirements.txt

2. Configure your application using the .env file

3. Run with Honcho

        $ honcho start

### Running commands

Run through Honcho, e.g:

    $ honcho run python manage.py syncdb

#### Environment Configuration

Honcho adds the following environment variables, update ``.env`` and ``dana/settings.py`` if you need more:

- ``DEBUG``, ``False`` - boolean that turns on/off debug mode
- ``PORT``, ``8000`` - port number for HTTP server
- ``WORKERS``, ``2`` - number of Gunicorn worker process for handling requests
- ``SITE_ID``, ``1`` - current Django site
- ``SECRET_KEY``, ``''`` - used in hashing algorithms, the longer the better
- ``DB_ENGINE``, ``''``- database backend, e.g. ``django.db.backends.mysql``
- ``DB_NAME``, ``''`` - database name
- ``DB_USER``, ``''`` - database user
- ``DB_PASSWORD``, ``''`` - database password
- ``DB_HOST``, ``''`` - database host, empty means localhost
- ``DB_PORT``, ``''`` - database port, empty means default
- ``TIME_ZONE``, ``'Europe/London'`` - [see available choices](http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE)
- ``LANGUAGE_CODE``, ``'en-gb'`` - language code for this installation
- ``USE_I18N``, ``False`` - enable Django's translation system
- ``USE_L10N``, ``True`` - localised data formatting
- ``USE_TZ``, ``True`` - specifies if datetimes will be timezone-aware

[See Django settings documentation](https://docs.djangoproject.com/en/1.4/ref/settings/)

**Note:** Django defaults are defined in ``dana/settings.py``, so you don't need to duplicate these in your ``.env`` if you want to keep it minimal.

#### Further reading:

- [The Twelve-Factor App](http://www.12factor.net/)
- [Declaring and Scaling Process Types with Procfile](https://devcenter.heroku.com/articles/procfile)
- [Applying the Unix Process Model to Web Apps](http://adam.heroku.com/past/2011/5/9/applying_the_unix_process_model_to_web_apps/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)










