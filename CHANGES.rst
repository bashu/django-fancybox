Changes
-------

0.2.0 (2026-11-13)
~~~~~~~~~~~~~~~~~~

* Build the package with ``hatchling`` instead of ``setuptools``.
* Move the package to the ``src`` layout; tests are no longer shipped in the distribution.
* Simplify the example project: it runs with ``uv`` and needs no database.
* Detect ajax requests in templates with ``request.headers.x_requested_with`` instead of
  ``request.is_ajax``, which was removed in Django 4.0. Update your templates the same way.

0.1.9 (2026-10-10)
~~~~~~~~~~~~~~~~~~

* Drop Python 3.10 support; Python 3.11 is now the minimum required version.

0.1.7 (2026-08-14)
~~~~~~~~~~~~~~~~~~

* Migrate packaging to ``pyproject.toml`` and modern tooling (ruff, pre-commit, tox, versionflow).
