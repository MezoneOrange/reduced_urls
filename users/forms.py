from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password


class UserRegistrationForm(UserCreationForm):
    """Form for user registration.

    email - email field, add email field to registration form.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}), label='Почта')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),
                                label='Пароль',
                                help_text=password_validation.password_validators_help_text_html(),
                                validators=[validate_password])

    def __init__(self, *args, **kwargs):
        """Delete passwors2 field from registration form."""
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'password1': forms.PasswordInput(attrs={'class': 'input'})
        }


class UserUpdateForm(forms.ModelForm):
    """Form for update user's profile.

    Allows change username and email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


