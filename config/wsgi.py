"""
WSGI config for ZACH main website project.

This module exposes the module-level variable ``application`` that cPanel's
"Setup Python App" (mod_wsgi) and any WSGI server use as the entry point.
The variable MUST be named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
