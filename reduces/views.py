from django.shortcuts import render
from django.views import View


class HomePage(View):
    """Home page realisation.

        reduces/home.html

    """
    def get(self, request):
        """For move to home page."""
        data = {
            'title': 'Домашняя страница',
        }
        return render(request, 'reduces/home.html', data)


class AboutPage(View):
    """About page realisation.

        reduces/about.html

    """
    def get(self, request):
        """For move to about page."""
        data = {
            'title': "О нас",
        }
        return render(request, 'reduces/about.html', data)
