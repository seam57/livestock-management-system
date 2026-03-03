from django.shortcuts import render
from django.shortcuts import render
from .models import Animal

def dashboard(request):
    # Database theke koyta Cow, Hen, ebong Goat ache ta count korbe
    total_cows = Animal.objects.filter(animal_type='Cow').count()
    total_hens = Animal.objects.filter(animal_type='Hen').count()
    total_goats = Animal.objects.filter(animal_type='Goat').count()
    
    context = {
        'total_cows': total_cows,
        'total_hens': total_hens,
        'total_goats': total_goats,
    }
    return render(request, 'farm/dashboard.html', context)

# Create your views here.
