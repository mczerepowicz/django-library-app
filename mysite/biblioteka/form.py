from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Czytelnik,Bibliotekarz, Autor, Ksiazka, Egzemplarz, Wydawnictwo, Jezyk, Gatunek, Ocena

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['imie', 'nazwisko', 'data_urodzenia', 'data_smierci']
        
class KsiazkaForm(ModelForm):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'gatunek']
        
class EgzemplarzForm(ModelForm):
    class Meta:
        model = Egzemplarz
        fields = ['data', 'wydawnictwo', 'jezyk', 'ksiazka', 'user']
        
class WydawnictwoForm(ModelForm):
    class Meta:
        model = Wydawnictwo
        fields = ['nazwa_wydawnictwa']
                
class JezykForm(ModelForm):
    class Meta:
        model = Jezyk
        fields = ['nazwa_jezyka']
                
class GatunekForm(ModelForm):
    class Meta:
        model = Gatunek
        fields = ['nazwa_gatunku']
        
class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['komentarz', 'egzemplarz']
        
class CzytelnikSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_czytelnik = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        czytelnik = Czytelnik.objects.create(user=user)
        czytelnik.phone_number=self.cleaned_data.get('phone_number')
        czytelnik.save()
        return user

class BibliotekarzSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_bibliotekarz = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        bibliotekarz = Bibliotekarz.objects.create(user=user)
        bibliotekarz.phone_number=self.cleaned_data.get('phone_number')
        bibliotekarz.save()
        return user