from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Autor(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.DateField('Data urodzenia')
    data_smierci = models.DateField('Data smierci', null=True, blank=True)
    
    def __str__(self):
        return '{0}, {1}'.format(self.imie, self.nazwisko)
    
class Gatunek(models.Model):
    nazwa_gatunku = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa_gatunku
    

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=100)
    
    autor = models.ManyToManyField(Autor)
    gatunek = models.ManyToManyField(Gatunek)
    
    def __str__(self):
        return self.tytul
    
    
class Wydawnictwo(models.Model):
    nazwa_wydawnictwa = models.CharField(max_length=100)
        
    def __str__(self):
        return self.nazwa_wydawnictwa

    
class Jezyk(models.Model):
    nazwa_jezyka = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nazwa_jezyka
    
class User(AbstractUser):
    is_czytelnik = models.BooleanField(default=False)
    is_bibliotekarz = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Czytelnik(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)

class Bibliotekarz(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    
class Egzemplarz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalny klucz')
    data = models.DateField('Data wydania', null=True, blank=True)
    wydawnictwo = models.ForeignKey(Wydawnictwo, on_delete=models.CASCADE)
    jezyk = models.ForeignKey(Jezyk, on_delete=models.CASCADE)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    DOSTEPNOSC_STATUS = (
        ('d', 'Dostepna'),
        ('nd', 'Niedostepna'),
    )

    status = models.CharField(
        max_length=2,
        choices=DOSTEPNOSC_STATUS,
        blank=True,
        default='d',
        help_text='Dostepnosc',
    )
    
    def __str__(self):
        return self.ksiazka.tytul
    
class Ocena(models.Model):
    komentarz = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    egzemplarz = models.ForeignKey(Egzemplarz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.komentarz
    




    
  