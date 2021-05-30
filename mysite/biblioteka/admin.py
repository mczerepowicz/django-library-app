from django.contrib import admin
from .models import Egzemplarz, Ksiazka, Autor, Jezyk, Gatunek, Wydawnictwo, Ocena, User, Czytelnik, Bibliotekarz

# Register your models here.
admin.site.register(Egzemplarz)
admin.site.register(Ksiazka)
admin.site.register(Wydawnictwo)
admin.site.register(Gatunek)
admin.site.register(Jezyk)
admin.site.register(Autor)
admin.site.register(Ocena)
admin.site.register(User)
admin.site.register(Czytelnik)
admin.site.register(Bibliotekarz)