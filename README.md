django-fancybox
===============

This is a [Django](https://www.djangoproject.com/) integration of [Fancybox](http://fancyapps.com/fancybox/).

[![Latest Version](https://pypip.in/version/django-fancybox/badge.svg)](https://pypi.python.org/pypi/django-fancybox/)
[![Downloads](https://pypip.in/download/django-fancybox/badge.svg)](https://pypi.python.org/pypi/django-fancybox/)
[![License](https://pypip.in/license/django-fancybox/badge.svg)](https://pypi.python.org/pypi/django-fancybox/)

## Installation

    $ pip install django-fancybox

### External dependencies

* jQuery - This is not included in the package since it is expected that in most scenarios this would already be available.

## Setup

Add `fancybox` to  `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
	...
	'fancybox',
]
```
Be sure you have the `django.core.context_processors.request` processor
```python
TEMPLATE_CONTEXT_PROCESSORS = [
	...
	"django.core.context_processors.request"
]
```
and just include `fancybox` templates
```html
{% include "fancybox/fancybox_css.html" %} {# Before the closing head tag #}
{% include "fancybox/fancybox_js.html" %} %} {# Before the closing body tag #}
```
When deploying on production server, don't forget to run :
```shell
$ python manage.py collectstatic
```    
## Usage

Extend base template for ajax requests
```html
{% extends request.is_ajax|yesno:"fancybox/base.html,base.html" %}
```
Add `class="fancybox"` to a link, and set the href to a page you want to display
```html
<a href="{% url 'remote.html' %}" class="fancybox">Click here</a>
```
Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

## License

`django-fancybox` is released under the BSD license.
