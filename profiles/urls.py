from django.urls import path
from . import views

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('usertuitions/', views.userTuitions, name='usertuitions'),
    path('adminaprove/<int:id>/', views.adminAcceptedtotuition, name='admin_aprove'),
    # path('details/', views.tuitionReview, name='detail_review'),
]
