.. image:: https://codecov.io/gh/aniketmaithani/django-custom-user-example/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aniketmaithani/django-custom-user-example

.. image:: https://travis-ci.org/aniketmaithani/django-custom-user-example.svg?branch=master
    :target: https://travis-ci.org/aniketmaithani/django-custom-user-example

.. image:: https://landscape.io/github/aniketmaithani/django-custom-user-example/master/landscape.svg?style=flat
   :target: https://landscape.io/github/aniketmaithani/django-custom-user-example/master
   :alt: Code Health

==========================
Django Custom User Example
==========================

This is an example Django project that demonstrates the configurable User model available in Django 1.5.  It is inspired by `Dr. Russell Keith-Magee's <https://github.com/freakboy3742>`_ talk at DjangoCon US 2013 `Red User, Blue User, MyUser, auth.User <https://speakerdeck.com/freakboy3742/red-user-blue-user-myuser-auth-dot-user>`_.

Getting Started
---------------
Clone this repository:
::

    $ git clone https://github.com/jonathanchu/django-custom-user-example.git
    $ cd django-custom-user-example

Create a virtual environment for this project and install Django (1.5.4+ recommended):
::

    $ mkvirtualenv customuser
    (customuser) $ pip install django

Run `syncdb` or `migrate` (depending on your Django version) and create a superuser when prompted:
(Django < 1.9)
::

    (customuser) $ python manage.py syncdb
    ...

(Django 1.9+)
::

    (customuser) $ python manage.py migrate
    ...
    (customuser) $ python manage.py createsuperuser
    ...

Run `runserver`:
::

    (customuser) $ python manage.py runserver



Finally, open up http://127.0.0.1:8000/admin in your browser and login with the superuser just created.  You should see your custom user under "Accounts".

Screenshots
-----------

.. image:: http://i.imgur.com/As2xDEg.png
.. image:: http://i.imgur.com/uaG4qaH.png


Running Tests Locally
-----------
 - Tests have been added to this sample project. You can install these tests from 
 `dev-requirements`. 
 - `Py.Test` has been integrated with the test suite. In order to run these tests just run the following command 
 `py.test` 

 - In case you want to see your test coverage, just run `py.test --cov` . 

Comments/Feedback
-----------------

Suggestions for any modifications, please feel free to fork and contribute!

Please file bugs at `https://github.com/jonathanchu/django-custom-user-example/issues <https://github.com/jonathanchu/django-custom-user-example/issues>`_.
