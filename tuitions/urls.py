from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_tuition, name='add_tuition'),
    # path('edit/<int:id>', views.edit_post, name='edit_post'),
    # path('delete/<int:id>', views.delete_post, name='delete_post'),
]
