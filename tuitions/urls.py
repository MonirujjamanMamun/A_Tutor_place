from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_tuition, name='add_tuition'),
    path('edit/<int:id>', views.edit_post, name='edit_tuition'),
    path('delete/<int:id>', views.delete_post, name='delete_tuition'),
    path('apply/<int:id>', views.userapplytotuition, name='apply_tuition'),
]
