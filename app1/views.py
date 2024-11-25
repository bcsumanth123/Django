from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse(f'<h1> this is multiple apps create</h1>')


def home_fun(request):
    return HttpResponse(f'<h1> this is multiple apps1 functions create</h1>')