from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):
    
    #permet d'afficher le nom sur la liste des models dans l'interface admin
    def __str__(self):
        return f'{self.name}'
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
class Listing(models.Model):
    
    #permet d'afficher le nom sur la liste des models dans l'interface admin
    def __str__(self):
        return f'{self.title}'
    
    class Type(models.TextChoices):
        Records = 'R'
        Clothing = 'C'
        Posters = 'P'
        Miscellaneous = 'M'
    
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=5000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)