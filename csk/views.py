from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1><marquee>Ruturaj is the captain of csk</marquee></h1>')
