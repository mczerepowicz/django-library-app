from django.db import models
import uuid

# Create your models here.

class Autor(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.DateField('Data urodzenia')
    data_smierci = models.DateField('Data smierci')
    
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
    
    
class Wydanie(models.Model):
    wydawnictwo = models.CharField(max_length=100)
    data = models.DateField('Data wydania')
    
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ksiazka.tytul

    
class Jezyk(models.Model):
    nazwa_jezyka = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nazwa_jezyka

class Ocena(models.Model):
    komentarz = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.komentarz
    
    
class Egzemplarz(models.Model):
    # 0 - niedostepny, 1-dostepny
    #dostepnosc = models.IntegerField(default=1)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalny klucz')
    wydanie = models.ForeignKey(Wydanie, on_delete=models.CASCADE)
    jezyk = models.ForeignKey(Jezyk, on_delete=models.CASCADE)
    ocena = models.ForeignKey(Ocena, on_delete=models.CASCADE)

    
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
    

    
#class Czytelnik(models.Model):




    
  