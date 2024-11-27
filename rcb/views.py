from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1 background color='red'><marquee>KING KOHLI WILL RAISE THE IPL TROPHY VERY SOOOON</marquee></h1>')