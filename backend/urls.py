from django.urls import path
from .import views

app_name = 'Ecommerce_Console'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.signIn, name="login"),
]