from django.shortcuts import render
from django.http import HttpResponse
from .models import Ksiazka

# Create your views here.



#def index(request):
#    return HttpResponse("Katalog biblioteki")


def index(request):
    #ksiazka_lista = Ksiazka.objects.order_by('tytul')
    ksiazka_lista = Ksiazka.objects.all()
    context = {'ksiazka_lista': ksiazka_lista}
    return render(request, 'biblioteka/index.html', context)