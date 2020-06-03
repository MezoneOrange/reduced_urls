from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm
from .forms import UserUpdateForm


class Registration(View):
    """Class for realisation user's registration."""
    def get(self, request):
        """for move to registration page."""
        form = UserRegistrationForm()
        data = {
            'title': 'Регистрация',
            'form': form,
        }
        return render(request, 'users/registration.html', data)

    def post(self, request):
        """for registration user in User model."""
        pass


class Profile(View):
    """Realisation User's profile page with data update function."""
    def get(self, request):
        """for move to profile page."""
        pass

    def post(self, request):
        """for update data in User model."""
        pass