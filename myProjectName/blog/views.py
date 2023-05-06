from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


# Create your views here.

def blog_root_view(request):
    rendered = render_to_string('blog_overview.html', {
        'message': 'Wellcome to my blog😁!'
    })
    # return HttpResponse("<h1>Wellcome to my blog😁!</h1>")
    return HttpResponse(rendered)


def categories_view(request):
    return HttpResponse("<h1>blog Categories 📃</h1>")


def animals_view(request):
    rendered = render_to_string('animals.html', {

    })
    return HttpResponse(rendered)