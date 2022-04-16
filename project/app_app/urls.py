from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_request, name='test'),
    path("login", views.login_request, name="login"),
    path("entry-list", views.EntryListView.as_view(), name="entry-list"),
    path("entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"),
]