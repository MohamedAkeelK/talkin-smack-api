from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmackCreateListView.as_view(), name='smack'),
    path('<int:smack_id>/', views.SmackDetailView.as_view(), name='smack_detail'),
]
