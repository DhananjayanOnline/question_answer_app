from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, ListView, FormView
from django.urls import reverse_lazy
from .forms import *
from core_app.models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        if form.is_valid:
            messages.success(self.request, 'Account has been created')
        else:
            messages.error(self.request, 'sign-up imformation is not valid')
        return super().form_valid(form)

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


class IndexView(CreateView, ListView):
    template_name = 'index.html'
    form_class = PostForm
    model = Questions
    context_object_name = 'questions'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Questions.objects.all().order_by('-date_created')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.is_valid():
            messages.success(self.request, 'New question has been asked')
        else:
            messages.error(self.request, 'Something went wrong, please try again')
        return super().form_valid(form)   

    
