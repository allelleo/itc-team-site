from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
# def home(request):


class Home(View):
    template_name = 'home/home.html'

    def get(self, request):
        context = {
            'phone': "+88005553535",
            'gmail': "VeryCoolCorp@smile.com",
            'vk_link': "https://vk.com/newsitc",
            "tg_link": "https://t.me/itskipfin"
        }
        return render(request, 'home/home.html', context=context)
