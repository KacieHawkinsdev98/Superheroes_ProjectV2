from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero



def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'Superhero/index.html', context)

def detail(request, superheros_id):
    superheros = Superhero.objects.get(pk=superheros_id)
    context = {
        "superheros":superheros
    }
    return render(request, 'Superhero/detail.html', context)
    

def create(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_super_ability = request.POST.get('primary_super_ability')
        secondary_super_ability = request.POST.get('secondary_super_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superheros = Superhero(name=name, alter_ego_name=alter_ego_name, primary_super_ability=primary_super_ability, secondary_super_ability=secondary_super_ability, catchphrase=catchphrase)
        new_superheros.save()
        return HttpResponseRedirect(reverse('Superhero:index'))
    else:
        return render(request, 'Superhero/create.html')


def delete(request, superheros_id):
    superheros = Superhero.objects.get(pk=superheros_id)
    if request.method == "POST":
        superheros.delete()
        return index(request)
    else:
        context = {
            "superheros": superheros
        }
        return render(request, 'Superhero/delete.html', context)


