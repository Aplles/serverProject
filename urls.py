from server.routing import path
from views import index, home

urlpatterns = [
    path("", index),
    path("home/", home),
]
