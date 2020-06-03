from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm
from .forms import UserUpdateForm


@login_required
class Profile(View):
    """Realisation User's profile page with data update function.

        users/profile.html

    """
    def get(self, request):
        """for move to profile page."""
        form = UserUpdateForm(instance=request.user)
        data = {
           'title': 'Личный кабинет',
            'form': form,
        }
        return render(request, 'users/profile.html', data)

    def post(self, request):
        """for update data in User model."""
        pass


def register(request):
    if request.method == "POST":  # если была нажата кнопка отправки формы
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # если форма была заполненна и удовлетворяет условиям
            form.save()  # сохранение пользователя
            username = form.cleaned_data.get("username")
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:  # когда просто перешли на страницу регистрации
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация'})