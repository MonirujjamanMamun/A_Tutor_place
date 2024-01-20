from django.urls import path
from . import views


urlpatterns = [
    path('user_review/<int:id>/', views.DetailPostView.as_view(), name='review'),
]
