
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmackView.as_view(), name='smack'),
    path('<int:smack_id>/', views.SmackIdView.as_view(), name='smack'),
    path('update-smack/<int:smack_id>/',
         views.UpdateSmackStatusView.as_view(), name='update_smack_status'),
    path('user/<int:user_id>/smack',
         views.UserSmackView.as_view(), name='users_smack'),
    # todo: work on this route
    path('user/<int:user_id>/smack/<int:smack_id>/',
         views.UserSmackDetailView.as_view(), name='user_smack_detail'),
]
