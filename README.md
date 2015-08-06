django-fancybox
===============

This is a [Django](https://www.djangoproject.com/) integration of [Fancybox](http://fancyapps.com/fancybox/).

Authored by [Basil Shubin](https://github.com/bashu)

[![Latest Version](https://img.shields.io/pypi/v/django-fancybox.svg)](https://pypi.python.org/pypi/django-fancybox/)
[![Downloads](https://img.shields.io/pypi/dm/django-fancybox.svg)](https://pypi.python.org/pypi/django-fancybox/)
[![License](https://img.shields.io/github/license/bashu/django-fancybox.svg)](https://pypi.python.org/pypi/django-fancybox/)
[![Code Health](https://landscape.io/github/bashu/django-fancybox/develop/landscape.svg?style=flat)](https://landscape.io/github/bashu/django-fancybox/develop)

## Installation
```shell
pip install django-fancybox
```
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
	"django.core.context_processors.request",
]
```
and just include `fancybox` templates
```html+django
{% include "fancybox/fancybox_css.html" %} {# Before the closing head tag #}
{% include "fancybox/fancybox_js.html" %} {# Before the closing body tag #}
```
When deploying on production server, don't forget to run :
```shell
python manage.py collectstatic
```    
## Usage

Extend base template for ajax requests
```html+django
{% extends request.is_ajax|yesno:"fancybox/base.html,base.html" %}
```
Add `class="fancybox"` to a link, and set the href to a page you want to display
```html+django
<a href="{% url 'remote.html' %}" class="fancybox">Click here</a>
```
Please see `example` application. This application is used to manually test the functionalities of this package. This also serves as a good example.

You need only Django 1.4 or above to run that. It might run on older versions but that is not tested.

## License

`django-fancybox` is released under the BSD license.
