# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect  # ajoutez cet import


# definition des differentes vue fonctionne comme le controller 

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})
    
def band_create(request):
    if reques.method == 'POST':
        
    form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})
   
def band_detail(request, id):
    # nous insérons cette ligne pour obtenir le Band avec cet id
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})  # nous mettons à jour cette ligne pour passer le groupe au gabarit


#controller de listing

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html',
                  {'listings': listings})


#controller about-us

def about(request):
    listings = Listing.objects.all()
    return render(request, 'listings/about.html')




# controller de contact


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
        
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})


#confirmation du formulaire

def validation(request):
    return render(request, 'listings/validation.html')