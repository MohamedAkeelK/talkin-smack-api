
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, get_object_or_404

from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:smack_id>/', views.SmackIdView.as_view(), name='smack'),
    path('update-smack/<int:smack_id>/',
         views.UpdateSmackStatusView.as_view(), name='update_smack_status'),
    path('user/<int:user_id>/smack',
         views.UserSmackView.as_view(), name='users_smack'),
    # todo: work on this route
    path('user/<int:user_id>/smack/<int:smack_id>/',
         views.UserSmackDetailView.as_view(), name='user_smack_detail'),
    # path('comment', views.CommentViewSet.as_view(), name='comment'),
]
