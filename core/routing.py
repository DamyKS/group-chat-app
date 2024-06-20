from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
import chat.routing

import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_application,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})