"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views


app_name = 'biblioteka'
urlpatterns = [
    path('', views.index, name='index'),
    path('ksiazki/', views.ksiazka, name='ksiazka'),
    path('<int:ksiazka_id>/egzemplarze', views.egzemplarze, name='egzemplarze'),
    path('<uuid:egz_id>/egzemplarzDetail', views.egzemplarzDetail, name='egzDetail'),
    #path('ksiazka_detail.html/<int:ksiazka_id>', views.ksiazkaDetail, name='ksiazkaDetail'),
    path('wydawnictwo/', views.wydawnictwo, name='wydawnictwo'),
    path('<int:wyd_id>/wydDetail', views.wydawnictwoDetail, name='wydDetail'),
    path('usunWyd/<int:wyd_id>', views.usunWydawnictwo, name='usunWyd'),
    path('edycjaWyd/<int:wyd_id>', views.edycjaWydawnictwo, name='edycjaWyd'),
    path('formularzWyd/', views.formWydawnictwo, name='formWyd'),
    path('jezyk/', views.jezyk, name='jezyk'),
    path('formularzJezyk/', views.formJezyk, name='formJezyk'),
    path('gatunek/', views.gatunek, name='gatunek'),
    path('<int:gat_id>/gatunekDetail', views.gatunekDetail, name='gatDetail'),
    path('formularzGatunek/', views.formGatunek, name='formGatunek'),
    path('usunGatunek/<int:gat_id>', views.usunGatunek, name='usunGat'),
    path('edycjaGatunek/<int:gat_id>', views.edycjaGatunek, name='edycjaGat'),
    path('autor/', views.autor, name='autor'),
    path('<int:autor_id>/autorDetail', views.autorDetail, name='autorDetail'),
    path('formularzAutor/', views.formAutor, name='formAutor'),
    path('usunAutor/<int:autor_id>', views.usunAutor, name='usun'),
    path('edycjaAutor/<int:autor_id>', views.edycjaAutor, name='edycja'),
    path('formularzKsiazka/', views.formKsiazka, name='formKsiazka'), 
    path('formularzEgz/', views.formEgzemplarz, name='formEgzemplarz'),
    path('usunEgz/<uuid:egz_id>', views.usunEgzemplarz, name='usun'),
    path('edycjaEgz/<uuid:egz_id>', views.edycjaEgzemplarz, name='edycja'),
    path('komEgz/<uuid:egz_id>', views.dodajKomentarz, name='komentarz'),
    path('register/',views.register, name='register'),
    path('customer_register/',views.czytelnik_register.as_view(), name='customer_register'),
    path('employee_register/',views.bibliotekarz_register.as_view(), name='employee_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
