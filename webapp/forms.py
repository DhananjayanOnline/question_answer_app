from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core_app.models import Questions, Answers

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'title',
            'describtion',
            'image',
        ]

        widgets={
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'describtion':forms.TextInput(attrs={"class":"form-control"}),
            'image':forms.FileInput(attrs={"class":"form-control"}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = [
            'answer',
        ]

        widgets = {
            'answer':forms.Textarea(attrs={'class': 'form-control', 'rows':5})
        }