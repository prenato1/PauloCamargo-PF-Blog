from django import forms
    
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='O email é obrigatório.')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'date_of_birth']
