# from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('all/', views.all_watches, name='all_watches'),
    path('create/', views.create_watch, name = 'create_watch'),
    path('detail/<int:pk>/', views.detail_watch, name = 'detail_watch'),
    path('update/<int:pk>/', views.update_watch, name = 'update_watch'),
    path('delete/<int:pk>/', views.delete_watch, name = 'delete_watch'),

]