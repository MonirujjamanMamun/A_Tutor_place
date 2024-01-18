
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserAccountUpdateView, pass_change, user_logout

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('update_profile/', UserAccountUpdateView.as_view(), name='update_profile'),
    path('password_change/', pass_change, name='pass_change')
]
