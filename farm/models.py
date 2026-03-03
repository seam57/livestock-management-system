from django.db import models
from django.db import models

class Animal(models.Model):
    ANIMAL_TYPES = [
        ('Hen', 'Hen'),
        ('Cow', 'Cow'),
        ('Goat', 'Goat'),
    ]

    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=10, choices=ANIMAL_TYPES)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Create your models here.
