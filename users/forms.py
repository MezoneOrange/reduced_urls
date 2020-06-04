from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.utils.safestring import mark_safe



class UserRegistrationForm(UserCreationForm):
    """Form for user registration.

    email - email field, add email field to registration form.
    """
    help_password_text = ("<ul class='help_list'>" +
                          "<li class='help_list_item'>Ваш пароль не должен совпадать с ваши именем" +
                          " или другой персональной информацией" +
                          " или быть слишком похожим на нее.</li>" +
                          "<li class='help_list_item'>Ваш пароль должен содержать как минимум 8 символов.</li>" +
                          "<li class='help_list_item'>Ваш пароль не может быть одним из" +
                          " широко распростарненных паролей.</li>" +
                          "<li class='help_list_item'>Ваш пароль не может состоять только из цифр.</li>" +
                          "</ul>")

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}),
                             label='Почта')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),
                                label='Пароль',
                                help_text=mark_safe(help_password_text),
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
        help_texts = {
            'email': "Текст для почты"
        }


class UserUpdateForm(forms.ModelForm):
    """Form for update user's profile.

    Allows change username and email.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}),
                             label='Почта',
                             validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
        }


class UserLoginForm(AuthenticationForm):
    """Customization for login form."""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Пароль')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        user = self.user_cache  # set by super class
        if user.my_class.expired:
            raise forms.ValidationError('This User has Expired!')
        return cleaned_data

