from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view(), name='signup'),
    path("login/", LoginView.as_view(), name='signin'),
    path("home/", IndexView.as_view(), name='home'),
]
