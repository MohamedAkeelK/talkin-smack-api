from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmackCreateListView.as_view(), name='smack'),
    # path('smack')
]
