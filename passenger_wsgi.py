import os
import sys

# Project root (the directory that contains this file). More reliable than
# os.getcwd(), which Passenger does not guarantee.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# 1. Force the application to use the uv-created virtualenv interpreter, if
#    present. cPanel/Passenger may otherwise launch with the system Python.
VENV_PYTHON = os.path.join(PROJECT_ROOT, ".venv", "bin", "python")
if os.path.exists(VENV_PYTHON) and sys.executable != VENV_PYTHON:
    os.execl(VENV_PYTHON, VENV_PYTHON, *sys.argv)

# 2. Add the project root to the path so the `config` package can be imported.
sys.path.insert(0, PROJECT_ROOT)

# 3. Use production settings.
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"

# 4. Build the WSGI application object (must be named `application`).
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
