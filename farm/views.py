from django.shortcuts import render, redirect  # 'redirect' add kora hoyeche
from .models import Animal
from .forms import AnimalForm  # 'AnimalForm' import kora hoyeche

def dashboard(request):
    # Database theke count korbe
    total_cows = Animal.objects.filter(animal_type='Cow').count()
    total_hens = Animal.objects.filter(animal_type='Hen').count()
    total_goats = Animal.objects.filter(animal_type='Goat').count()
    
    context = {
        'total_cows': total_cows,
        'total_hens': total_hens,
        'total_goats': total_goats,
    }
    return render(request, 'farm/dashboard.html', context)

def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('dashboard') 
    else:
        form = AnimalForm()
    return render(request, 'farm/add_animal.html', {'form': form})