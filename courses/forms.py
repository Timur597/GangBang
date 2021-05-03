from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Courses
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# from captcha.fields import CaptchaField
#
#
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     mobile = forms.IntegerField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#
#     captcha = CaptchaField()