import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')typo
import django 
django.setup()
from django.core.asgi import get_asgi_application



application = get_asgi_application()
