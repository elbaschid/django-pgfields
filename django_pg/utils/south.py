from __future__ import absolute_import, unicode_literals
import django

try:
    import south
    south_installed = True
except ImportError:
    south_installed = False


if django.VERSION[1] < 7:
    using_new_migrations = False
else:
    using_new_migrations = True
