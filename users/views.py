from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegistrationForm
from .forms import UserUpdateForm


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

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
        data = {
            'title': 'Регистрация',
            'form': form,
        }
        return render(request, self.template_name, data)


class ProfileUpdate(LoginRequiredMixin, View):
    form_class = UserUpdateForm
    model = User
    template_name = 'users/profile.html'

    def get(self, request):
        form = self.form_class(instance=request.user)
        data = {
            'title': 'Личный кабинет',
            'form': form
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
        data = {
            'title': 'Личный кабинет',
            'form': form
        }
        return render(request, self.template_name, data)
