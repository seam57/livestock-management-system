from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'animal_type', 'breed', 'age', 'purchase_date', 'purchase_price']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }