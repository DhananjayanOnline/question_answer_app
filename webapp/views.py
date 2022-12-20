from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import *
from core_app.models import *
from django.contrib.auth import authenticate, login

# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            "form":form,
        }
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('signin')
        else:
            return render(request, "register.html", {"form":form})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            "form":form,
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request, usr)
                return redirect('home')
            else:
                print('login failed')
                return redirect('signin')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        qs = Questions.objects.all()
        return render(request, 'index.html', {'questions':qs})