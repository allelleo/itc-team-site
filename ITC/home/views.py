from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import FeedBack


# Create your views here.
# def home(request):


class Home(View):
    template_name = 'home/home.html'

    def get_context(self):
        return {
            'phone': "+88005553535",
            'gmail': "VeryCoolCorp@smile.com",
            'vk_link': "https://vk.com/newsitc",
            "tg_link": "https://t.me/itskipfin"
        }

    def get_client_ip(self, request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get(self, request):
        return render(request, 'home/home.html', context=self.get_context())

    def post(self, request):
        username = request.POST.get('username')
        gmail = request.POST.get('email')
        message = request.POST.get('message')
        if all([username, gmail, message]):
            NewFeedBack = FeedBack(ip=self.get_client_ip(request), username=username, gmail=gmail, message=message)
            NewFeedBack.save()

        return render(request, 'home/home.html', context=self.get_context())
