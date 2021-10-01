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
    superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        "selected_hero":superhero
    }
    return render(request, 'Superhero/detail.html', context)
    

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_super_ability = request.POST.get('primary_super_ability')
        secondary_super_ability = request.POST.get('secondary_super_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego_name=alter_ego_name, primary_super_ability=primary_super_ability, secondary_super_ability=secondary_super_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superhero:index'))
    else:
        return render(request, 'Superhero/create.html')

def edit(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    if request.method == "POST":
       superhero.name = request.POST.get('name')
       superhero.alter_ego_name = request.POST.get('alter_ego_name')
       superhero.primary_super_ability = request.POST.get('primary_super_ability')
       superhero.secondary_super_ability = request.POST.get('secondary_super_ability')
       superhero.catchphrase = request.POST.get('catchphrase')
       superhero.save()
       context = {
          "superhero":superhero
        }
       return render(request, 'Superhero/detail.html', context)
    else:
        context = {
           "superhero":superhero
        }
        return render(request, 'Superhero/edit.html', context)

def delete(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    if request.method == "POST":
        superhero.delete()
        return index(request)
    else:
        context = {
            "superhero": superhero
        }
        return render(request, 'Superhero/delete.html', context)

