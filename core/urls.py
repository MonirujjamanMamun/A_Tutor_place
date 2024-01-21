from django.urls import path
from . import views


urlpatterns = [
    path('contuct_us/', views.ContuctUs.as_view(), name='contuct'),
    path('about_us/', views.AboutUs.as_view(), name='about'),
]
