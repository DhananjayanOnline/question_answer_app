from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here.

class Registration(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

