from django.urls import path
from . import views as account_views

urlpatterns = [
    path('login/', account_views.sign_in, name='login'),
    path('logout/', account_views.sign_out, name='logout'),
    path('register/', account_views.register, name='register'),
]


