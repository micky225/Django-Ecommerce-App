from django.urls import path
from .import views

app_name = 'Ecommerce_Console'

urlpatterns = [
    path('', views.home, name="name")
]