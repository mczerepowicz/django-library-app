from django.contrib import admin
from .models import Egzemplarz, Ksiazka, Autor, Jezyk, Gatunek, Wydanie, Ocena

# Register your models here.
admin.site.register(Egzemplarz)
admin.site.register(Ksiazka)
admin.site.register(Wydanie)
admin.site.register(Gatunek)
admin.site.register(Jezyk)
admin.site.register(Autor)
admin.site.register(Ocena)