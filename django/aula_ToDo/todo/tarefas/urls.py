from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nova/$', views.nova_categoria, name='nova_categoria'),
]
