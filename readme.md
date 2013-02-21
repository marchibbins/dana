## Dana

A basic [Twelve-Factor](http://www.12factor.net/) Django application.

### Dependencies

- [Django](https://www.djangoproject.com/) - Python Web framework
- [Gunicorn](http://gunicorn.org/) - WSGI HTTP server
- [Honcho](https://github.com/nickstenning/honcho) - a Python clone of [Foreman](http://ddollar.github.com/foreman/)

### Run

1. Install requirements (use [virtualenv](https://pypi.python.org/pypi/virtualenv))

    $ pip install -r requirements.txt

2. Configure your application using the .env file

3. Run with Honcho

    $ honcho start

Further reading:

- [The Twelve-Factor App](http://www.12factor.net/)
- [Declaring and Scaling Process Types with Procfile](https://devcenter.heroku.com/articles/procfile)
- [Applying the Unix Process Model to Web Apps](http://adam.heroku.com/past/2011/5/9/applying_the_unix_process_model_to_web_apps/)

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)
