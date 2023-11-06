from django.urls import path
from .import views

app_name = 'Ecommerce_Console'

urlpatterns = [
    path('', views.home, name="name"),
    path('login/', views.signIn, name="login"),
    path('register/', views.signUp, name="register"),
    
]