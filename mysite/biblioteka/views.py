from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .form import CzytelnikSignUpForm, BibliotekarzSignUpForm, AutorForm, KsiazkaForm, EgzemplarzForm, WydawnictwoForm, JezykForm, GatunekForm, OcenaForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Ksiazka, Wydawnictwo, Egzemplarz, Autor, Bibliotekarz, Czytelnik, Gatunek, Jezyk, Ocena
from django.contrib.auth.decorators import login_required
from .decorators import czytelnik_required, bibliotekarz_required

# Create your views here.


def index(request):
    return render(request, 'biblioteka/index.html')

def ksiazka(request):
    ksiazka_lista = Ksiazka.objects.all()
    context = {'ksiazka_lista': ksiazka_lista}
    return render(request, 'biblioteka/ksiazki.html', context)

def wydawnictwo(request):
    wyd_lista = Wydawnictwo.objects.all()
    return render(request, 'biblioteka/wydawnictwo.html', {'wyd_lista': wyd_lista})

def wydawnictwoDetail(request, wyd_id):
    wydawnictwo = get_object_or_404(Wydawnictwo, pk=wyd_id)
    return render(request, 'biblioteka/wydawnictwoDetail.html', {'wyd': wydawnictwo})

def jezyk(request):
    jezyk_lista = Jezyk.objects.all()
    return render(request, 'biblioteka/jezyk.html', {'jezyk_lista': jezyk_lista})

def gatunek(request):
    gat_lista = Gatunek.objects.all()
    return render(request, 'biblioteka/gatunek.html', {'gat_lista': gat_lista})

def gatunekDetail(request, gat_id):
    gatunek = get_object_or_404(Gatunek, pk=gat_id)
    return render(request, 'biblioteka/gatunekDetail.html', {'gatunek': gatunek})

def egzemplarze(request, ksiazka_id):
    egzemplarz_lista = Egzemplarz.objects.all()
    ksiazka = get_object_or_404(Ksiazka, pk=ksiazka_id)
    gatunek_lista = ksiazka.gatunek.all()
    autor_lista = ksiazka.autor.all()
    context ={'egzemplarz_lista': egzemplarz_lista, 'ksiazka': ksiazka, 'gatunek_lista': gatunek_lista,
              'autor_lista': autor_lista}
    return render(request, 'biblioteka/egzemplarze.html', context)

def egzemplarzDetail(request, egz_id):
    egzemplarz = get_object_or_404(Egzemplarz, pk=egz_id)
    ocena_lista = Ocena.objects.all()
    return render(request, 'biblioteka/egzemplarzDetail.html', {'egz': egzemplarz, 'ocena_lista': ocena_lista})

def autor(request):
    autor_lista = Autor.objects.all()
    context = {'autor_lista': autor_lista}
    return render(request, 'biblioteka/autor.html', context)

def autorDetail(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'biblioteka/autorDetail.html', {'autor': autor})


def formAutor(request):
    formularz = AutorForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'biblioteka/formularz.html', {'form': formularz}) 
        
def edycjaAutor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    formularz = AutorForm(request.POST or None, request.FILES or None, instance = autor)
    if formularz.is_valid():
        formularz.save()
        return redirect('biblioteka:autor')
    return render(request, 'biblioteka/edycja.html', {'form': formularz})
    
def usunAutor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == "POST":
        autor.delete()
        return redirect('biblioteka:autor')
    return render(request, 'biblioteka/usun.html', {'autor_id': autor_id})

def formKsiazka(request):
    formularz = KsiazkaForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'biblioteka/formularz.html', {'form': formularz})

def formEgzemplarz(request):
    formularz = EgzemplarzForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'biblioteka/formularz.html', {'form': formularz})

def edycjaEgzemplarz(request, egz_id):
    egzemplarz = get_object_or_404(Egzemplarz, pk=egz_id)
    formularz = EgzemplarzForm(request.POST or None, request.FILES or None, instance = egzemplarz)
    if formularz.is_valid():
        formularz.save()
        return redirect('biblioteka:egzemplarze')
    return render(request, 'biblioteka/edycja.html', {'form': formularz})
    
def usunEgzemplarz(request, egz_id):
    egzemplarz = get_object_or_404(Egzemplarz, pk=egz_id)
    if request.method == "POST":
        egzemplarz.delete()
        return redirect('biblioteka:ksiazka')
    return render(request, 'biblioteka/usun.html')

def dodajKomentarz(request, egz_id):
    egzemplarz = get_object_or_404(Egzemplarz, pk=egz_id)
    formularz = OcenaForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        o = Ocena(komentarz = formularz.cleaned_data['komentarz'], user = request.user)
        o.save()
        egzemplarz.ocena = o
    return render(request, 'biblioteka/formularz.html', {'form': formularz}) 

def formWydawnictwo(request): 
    formularz = WydawnictwoForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'biblioteka/formularz.html', {'form': formularz})

def edycjaWydawnictwo(request, wyd_id):
    wydawnictwo = get_object_or_404(Wydawnictwo, pk=wyd_id)
    formularz = WydawnictwoForm(request.POST or None, request.FILES or None, instance = wydawnictwo)
    if formularz.is_valid():
        formularz.save()
        return redirect('biblioteka:wydawnictwo')
    return render(request, 'biblioteka/edycja.html', {'form': formularz})
    
def usunWydawnictwo(request, wyd_id):
    wydawnictwo = get_object_or_404(Wydawnictwo, pk=wyd_id)
    if request.method == "POST":
        wydawnictwo.delete()
        return redirect('biblioteka:wydawnictwo')
    return render(request, 'biblioteka/usun.html', {'wyd_id': wyd_id})

def formJezyk(request): 
    formularz = JezykForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'biblioteka/formularz.html', {'form': formularz})

def formGatunek(request): 
    formularz = GatunekForm(request.POST or None)
    if formularz.is_valid():
        formularz.save()
    return render(request, 'biblioteka/formularz.html', {'form': formularz})

def edycjaGatunek(request, gat_id):
    gatunek = get_object_or_404(Gatunek, pk=gat_id)
    formularz = GatunekForm(request.POST or None, request.FILES or None, instance = gatunek)
    if formularz.is_valid():
        formularz.save()
        return redirect('biblioteka:gatunek')
    return render(request, 'biblioteka/edycja.html', {'form': formularz})
    
def usunGatunek(request, gat_id):
    gatunek = get_object_or_404(Gatunek, pk=gat_id)
    if request.method == "POST":
        gatunek.delete()
        return redirect('biblioteka:gatunek')
    return render(request, 'biblioteka/usun.html', {'gat_id': gat_id})

def register(request):
    return render(request, 'biblioteka/register.html')

class czytelnik_register(CreateView):
    model = User
    form_class = CzytelnikSignUpForm
    template_name = 'biblioteka/czytelnik_rejestracja.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('biblioteka:index')

class bibliotekarz_register(CreateView):
    model = User
    form_class = BibliotekarzSignUpForm
    template_name = 'biblioteka/bibliotekarz_rejestracja.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('biblioteka:index') 


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('biblioteka:index')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'biblioteka/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('biblioteka:index')