from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='plovak-home'),
    path('o-nama/', views.about, name='plovak-about'),
    path('proizvodi/', views.proizvodi, name='plovak-proizvodi'),
    path('kontakt/', views.contact, name='plovak-contact'),
    path('proizvodi/stapovi/', views.stapovi, name='proizvodi-stapovi'),
    path('proizvodi/masinice/', views.masinice, name='proizvodi-masinice'),
    path('proizvodi/udice/', views.udice, name='proizvodi-udice'),
    path('proizvodi/strune/', views.strune, name='proizvodi-strune'),
    path('proizvodi/plovci/', views.plovci, name='proizvodi-plovci'),
    path('proizvodi/mamci/', views.mamci, name='proizvodi-mamci'),
    path('proizvodi/hrana/', views.hrana, name='proizvodi-hrana'),
    path('proizvodi/varalice/', views.varalice, name='proizvodi-varalice'),
    path('proizvodi/ostalo/', views.ostalo, name='proizvodi-ostalo'),
]