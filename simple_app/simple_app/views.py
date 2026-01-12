from django.http import HttpResponse
from django.shortcuts import render

# def homepage(request):
#     return HttpResponse("hello")

# def about(request):
#     return HttpResponse("first django app")

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')