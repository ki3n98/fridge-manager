from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='LoginPage'),
    path('', views.coverPage, name='coverPage')
]