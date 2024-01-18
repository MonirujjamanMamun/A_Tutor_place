from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='user_profiles'),
    path('adminaprove/<int:id>/', views.adminAcceptedtotuition, name='admin_aprove'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_review'),
]
