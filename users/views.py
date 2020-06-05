from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import UserRegistrationForm
from .forms import UserUpdateForm
from .forms import UserLoginForm


class RegisterUser(View):
    form_class = UserRegistrationForm
    model = User
    template_name = 'users/registration.html'

    def get(self, request):
        form = self.form_class()
        data = {
            'title': 'Регистрация',
            'form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request):
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
    form_class = UserUpdateForm
    model = User
    template_name = 'users/profile.html'

    @method_decorator(login_required)
    def get(self, request):
        form = self.form_class(instance=request.user)
        data = {
            'title': 'Личный кабинет',
            'form': form
        }
        return render(request, self.template_name, data)

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
        messages.error(request, f'Пользователь при обновлении профиля произошла ошибка')
        data = {
            'title': 'Личный кабинет',
            'form': form
        }
        return render(request, self.template_name, data)


def login(request):
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
