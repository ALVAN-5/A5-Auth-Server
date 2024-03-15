from django.urls import path
from . import views

urlpatterns = [
    path("createSession/", views.createSession, name="create session"),
    path("createSession/token/", views.createSessionFromToken, name="create session with token"),
    path("validateSession/<str:session_key>/", views.validateSession, name="validate session"),
    path("createIPUser/", views.createIPUser, name="create IP User"),
    path("resetIPToken/", views.resetIPToken, name="reset IP token"),
    path("removeIPUser/", views.removeIPUser, name="remove IP user")
]
