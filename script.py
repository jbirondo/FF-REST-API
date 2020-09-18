import sys

try:
    import requests
except ImportError:
    sys.exit(
        'requests was not properly installed. Try again. Are you sure you are in a venv?')
