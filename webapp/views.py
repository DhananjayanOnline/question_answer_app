from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, ListView, FormView
from django.urls import reverse_lazy
from .forms import *
from core_app.models import *
from django.contrib.auth import authenticate, login

# Create your views here.

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('signin')

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm


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


class IndexView(ListView):
    template_name = 'index.html'
    model = Questions
    context_object_name = 'questions'
    