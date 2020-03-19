from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'home.html')


def password(request):
    realpassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    for count in range(length):
        realpassword += random.choice(characters)
    return render(request, 'password.html',{'password':realpassword})


def about(request):
    return render(request, 'about.html')
