from django.urls import path
from . import views

urlpatterns = [
    path('usertuitions/', views.userTuitions, name='usertuitions'),
    path('adminaprove/<int:id>/', views.adminAcceptedtotuition, name='admin_aprove'),
    path('user/<int:user_id>/', views.user_profile, name='profile'),
]
