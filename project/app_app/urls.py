from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_request, name='test'),
    path("login", views.login_request, name="login")
]