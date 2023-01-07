from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def say_hello(request):
    ctx = {'name': 'Hello'}
    return render(request, 'playground/hello.html', ctx)