from sendsms import api

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about(request):
    
    api.send_sms(body='I can haz txt', from_phone='+254713395537', to=['+254795433859'], flash=True)
    return render(request, 'home/about.html')