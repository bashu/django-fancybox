django-fancybox
===============

This is a Django_ integration of Fancybox_.

.. image:: https://img.shields.io/pypi/v/django-fancybox.svg
    :target: https://pypi.python.org/pypi/django-fancybox/

.. image:: https://img.shields.io/pypi/dm/django-fancybox.svg
    :target: https://pypi.python.org/pypi/django-fancybox/

.. image:: https://img.shields.io/github/license/bashu/django-fancybox.svg
    :target: https://pypi.python.org/pypi/django-fancybox/

Installation
------------

.. code-block:: shell

    pip install django-fancybox
    
External dependencies
~~~~~~~~~~~~~~~~~~~~~

* jQuery - This is not included in the package since it is expected that in most scenarios this would already be available.

Setup
-----

Add ``fancybox`` to  ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'fancybox',
    )

Be sure you have the ``django.template.context_processors.request`` processor

.. code-block:: python

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

and just include ``fancybox`` templates

.. code-block:: html+django

    {% include "fancybox/fancybox_css.html" %} {# Before the closing head tag #}
    {% include "fancybox/fancybox_js.html" %} {# Before the closing body tag #}

When deploying on production server, don't forget to run :

.. code-block:: shell

    python manage.py collectstatic

Usage
-----

Extend base template for ajax requests

.. code-block:: html+django

    {% extends request.is_ajax|yesno:"fancybox/base.html,base.html" %}

Add ``class="fancybox"`` to a link, and set the href to a page you want to display

.. code-block:: html+django

    <a data-fancybox data-type="ajax" href="{% url 'remote.html' %}" class="fancybox">Click here</a>

Please see ``example`` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

License
-------

``django-fancybox`` is released under the BSD license.

.. _django: https://www.djangoproject.com/
.. _fancybox: http://fancyapps.com/fancybox/
