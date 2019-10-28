
from django.shortcuts import render, redirect
# Create your views here.



def contact(request):
    return render(request, 'home/contact.html')