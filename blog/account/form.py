from django import forms
from account.models import Profile
from django.contrib.auth.models import User
"""
    User Data Update
"""
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email")
"""
    Profile Update Form
"""
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profilepic","phone","bio")