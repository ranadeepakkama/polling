from django import forms
from django.contrib.auth.models import User
from .models import Polling
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class newForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']

class userCreatedPollFm(ModelForm):
    class Meta:
        model = Polling
        fields = ['question','option1','option2','option3']