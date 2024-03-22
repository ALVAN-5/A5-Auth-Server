from django.urls import path
from . import views

urlpatterns = [
    path("", views.healthCheck, name="health check"),
]
