import math

from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from .models import Question, Answer, Tag, Profile, QuestionManager
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.urls import reverse


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=4, widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data['password']
        if data == 'wrongpass':
            raise ValidationError('Wrong password')
        return data


class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=4, widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        if password != password_check:
            raise ValidationError('Password do not match')

        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('User already exists!')


    def save(self, **kwargs):
        self.cleaned_data.pop('password_check')
        return User.objects.create_user(**self.cleaned_data)
