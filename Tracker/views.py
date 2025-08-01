from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout

# Create your views here.

def home(request):
    return HttpResponse('helooo world.')
