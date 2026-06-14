from django.urls import path
from . import views

urlpatterns = [
    path('', views.homework_list, name='homework_list'),
    path('add/', views.homework_create, name='homework_create'),
    path('edit/<int:pk>/', views.homework_update, name='homework_update'),
    path('delete/<int:pk>/', views.homework_delete, name='homework_delete'),
]