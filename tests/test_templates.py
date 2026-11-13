from django.contrib.staticfiles.finders import find

import pytest


@pytest.mark.parametrize(
    "asset_path",
    [
        pytest.param("fancybox/css/jquery.fancybox.min.css", id="css"),
        pytest.param("fancybox/js/jquery.fancybox.min.js", id="js"),
    ],
)
def test_static_asset_is_discoverable(asset_path: str) -> None:
    assert find(asset_path) is not None
