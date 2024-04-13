from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def learn_python(request):
    return HttpResponse("<h1>Learn Python</h1>")