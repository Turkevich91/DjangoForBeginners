from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from blog.models import Animal


# Create your views here.
class AnimalView(View):
    template_name = 'animal_catalog.html'

    def get(self, request):
        animals = Animal.objects.all()
        return render(request, self.template_name, {'animals': animals})


class AnimalDetailView(View):
    template_name = 'animal_detail.html'

    def get(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)
        return render(request, self.template_name, {'animal': animal})

    def post(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)
        data = request.POST
        name = data['name']
        comment = data['comment']
        print(name, 'left the comment on ', animal.name, 'page: ',  comment)
        return HttpResponseRedirect(request.path)


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
