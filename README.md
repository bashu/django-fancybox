Django-Fancybox
===============

This is a [Django](https://www.djangoproject.com/) integration of [Fancybox](http://fancyapps.com/fancybox/).

[![Latest Release](https://pypip.in/v/django-fancybox/badge.png)](https://crate.io/package/django-fancybox)
[![Downloads](https://pypip.in/d/django-fancybox/badge.png)](https://crate.io/package/django-fancybox)

## Installation

    $ pip install django-fancybox

### External dependencies

* jQuery - This is not included in the package since it is expected that in most scenarios this would already be available.

## Setup

Add `fancybox` to  `INSTALLED_APPS`:

    INSTALLED_APPS = [
		...
    	'fancybox',
	]

Be sure you have the `django.core.context_processors.request` processor

	TEMPLATE_CONTEXT_PROCESSORS = [
		..
    	"django.core.context_processors.request"
	]

and just include `fancybox` templates

    {% include "fancybox/fancybox_css.html" %} {# Before the closing head tag #}
    {% include "fancybox/fancybox_js.html" %} %} {# Before the closing body tag #}

When deploying on production server, don't forget to run :

    $ python manage.py collectstatic
    
## Usage

Extend base template for ajax requests

    {% extends request.is_ajax|yesno:"fancybox/base.html,base.html" %}

Add `rel="fancybox"` to a link, and set the href to a page you want to display

    <a href="{% url 'remote.html' %}" class="fancybox">Click here</a>

Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

## License

`django-fancybox` is released under the BSD license.
