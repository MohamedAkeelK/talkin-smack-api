from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloSmackView.as_view(), name='hello_smack'),
]
