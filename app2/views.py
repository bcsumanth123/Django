from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def app2_fun(request):
    return HttpResponse(f'<h1> this is multiple apps1 and app2 functions create</h1>')


def sum1_fun(request):
    x = int(input('enter a number1'))
    y = int(input('enter a number2'))
    z = x + y

    return HttpResponse(f'<h1>sum of {x} and {y} is {z} </h1>')
