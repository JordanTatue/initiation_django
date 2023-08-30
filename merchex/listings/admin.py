# listings/admin.py

from django.contrib import admin
from listings.models import Listing
from listings.models import Band

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('id','name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la Band

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument

class ListingAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('id', 'title','band') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Listing, ListingAdmin)  # nous modifions cette ligne, en ajoutant un deuxième argument