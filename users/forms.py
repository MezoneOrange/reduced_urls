from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """Form for user registration.

    email - email field, add email field to registration form.
    """
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        """Delete passwors2 field from registration form."""
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    """Form for update user's profile.

    Allows change username and email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
