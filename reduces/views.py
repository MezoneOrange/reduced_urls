from django.shortcuts import render
from django.views import View


class HomePage(View):

    def get(self, request):
        data = {
            'title': 'Домашняя страница',
        }
        return render(request, 'reduces/home.html', data)
