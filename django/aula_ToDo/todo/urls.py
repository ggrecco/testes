from django.conf.urls import url
from django.contrib import admin

from todo.core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', views.home),
]
