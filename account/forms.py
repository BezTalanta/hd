from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.Form):
    '''
    Simple low-level user form, only for one main purpose - write less code
    '''

    username = forms.CharField(label='Username',
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Username here'
                                   }
                               ))
    password = forms.CharField(label='Password',
                               widget=forms.TextInput(
                                   attrs={
                                       'type': 'password',
                                       'placeholder': 'Password here'
                                   }
                               ))
