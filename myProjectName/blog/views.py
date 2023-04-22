from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog_root_view(request):
    return HttpResponse("<h1>Wellcome to my blog😁!</h1>")


def categories_view(request):
    return HttpResponse("<h1>blog Categories 📃</h1>")
