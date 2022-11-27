from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('smack/', include('smack.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
