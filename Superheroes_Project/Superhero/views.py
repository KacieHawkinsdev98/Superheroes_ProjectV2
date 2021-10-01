from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero



def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'hero/index.html', context)

def detail(request, superhero_id):
    superheros = Superhero.objects.get(pk=superhero_id)
    context = {
        "superheros":superheros
    }
    return render(request, 'Superhero/detail.html', context)
    

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_super_ability = request.POST.get('primary_super_ability')
        secondary_super_ability = request.POST.get('secondary_super_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superheros = Superhero(name=name, alter_ego_name=alter_ego_name, primary_super_ability=primary_super_ability, secondary_super_ability=secondary_super_ability, catchphrase=catchphrase)
        new_superheros.save()
        return HttpResponseRedirect(reverse('superhero:index'))
    else:
        return render(request, 'Superhero/create.html')

def edit(request, superheros_id):
    superheros = Superhero.objects.get(pk=superheros_id)
    if request.method == "POST":
       superheros.name = request.POST.get('name')
       superheros.alter_ego_name = request.POST.get('alter_ego_name')
       superheros.primary_super_ability = request.POST.get('primary_super_ability')
       superheros.secondary_super_ability = request.POST.get('secondary_super_ability')
       superheros.catchphrase = request.POST.get('catchphrase')
       superheros.save()
       context = {
          "superheroes": superheros
        } 
       return render(request, 'Superhero/detail.html', context)
    else:
        context = {
           "superheros":superheros
        }
        return render(request, 'Superhero/edit.html', context)

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

