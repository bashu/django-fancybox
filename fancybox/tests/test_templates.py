from django.contrib.staticfiles.finders import find
from django.test import TestCase


class FancyboxTemplateTestCase(TestCase):
    def test_static_assets_are_discoverable(self):
        assert find("fancybox/css/jquery.fancybox.min.css") is not None
        assert find("fancybox/js/jquery.fancybox.min.js") is not None
