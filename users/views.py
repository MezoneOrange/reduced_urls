from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django import forms

from .models import Link
from .forms import UserRegistrationForm
from .forms import UserUpdateForm
from .forms import UserLoginForm
from .forms import UserLinksForm


class RegisterUser(View):
    """For registration page.

    For display registration form and work with it. Saves new user to User model.

    form_class - class that using for display form. (UserRegistrationForm)

    model - model with that works the class. (User)

    template_name - html template that using for work with registration. (users/registration.html)

    """
    form_class = UserRegistrationForm
    model = User
    template_name = 'users/registration.html'

    def get(self, request):
        """Used when you just move to the page."""
        form = self.form_class()
        data = {
            'title': 'Регистрация',
            'form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request):
        """Used when you send data from the page."""
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('auth')
        messages.error(request, f'Пользователь при создании пользователя произошла ошибка')
        data = {
            'title': 'Регистрация',
            'form': form,
        }
        return render(request, self.template_name, data)


class ProfileUpdate(LoginRequiredMixin, View):
    """For profile page.

    For display profile of authorised user and work with his username and email.
    Allows to change user's username and email.

    form_class - class that using for display form. (UserUpdateForm)

    model - model with that works the class. (User)

    template_name - html template that using for work with registration. (users/profile.html)

    """
    form_class = UserUpdateForm
    model = User
    template_name = 'users/profile.html'

    @method_decorator(login_required)
    def get(self, request):
        """Used when you just move to the page. Displays current user's information in the form fields."""
        item = User.objects.filter(username=self.request.user).values()[0]
        name = item['username']
        email = item['email']
        form = self.form_class(instance=request.user)
        data = {
            'title': 'Личный кабинет',
            'form': form,
            'name': name,
            'email': email
        }

        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request):
        """Used when you send changed data from the page."""
        item = User.objects.filter(username=self.request.user).values()[0]
        name = item['username']
        email = item['email']
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
        messages.error(request, f'Пользователь при обновлении профиля произошла ошибка')
        data = {
            'title': 'Личный кабинет',
            'form': form,
            'name': name,
            'email': email
        }
        return render(request, self.template_name, data)


class UserLinks(LoginRequiredMixin, CreateView):
    model = Link
    fields = ['long_link', 'reduced_link']
    template_name = 'users/links.html'
    context_object_name = 'form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UserLinks, self).form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(UserLinks, self).get_form(form_class)
        form.fields['long_link'].widget = forms.TextInput(attrs={'placeholder': 'Введите ссылку',
                                                                 'class': 'input'})
        form.fields['reduced_link'].widget = forms.TextInput(attrs={'placeholder': 'Введите сокращение',
                                                                    'class': 'input'})
        return form

    def get_context_data(self, **kwards):
        # передача доп данных
        context = super(UserLinks, self).get_context_data(**kwards)
        context['title'] = f"Ссылки {self.kwargs.get('username')}"
        context['links'] = list(Link.objects.filter(author=self.request.user).values())
        return context


def login(request):
    """Works with authorisation form.

        users/auth.html

    Allows to move to authorization page and to authorise user if sent data would be correct.

    """
    error_message = ("<ul class='help_list'><li class='help_list_item'>" +
                     "Пожалуйста, введите правильно имя пользователя и пароль." +
                     " Оба поля могут быть чувствительны к регистру.</li></ul>")
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('profile')
        else:
            messages.error(request, mark_safe(error_message))
            return redirect('profile')

    else:
        form = UserLoginForm()
    return render(request, 'users/auth.html', {'form': form})
