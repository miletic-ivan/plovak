from django.shortcuts import render
from .models import Stapovi, Masinice, Udice, Hrana, Varalice, Ostalo, Plovci, Mamci, Strune

def home(request):
    return render(request, 'home/home.html')

def proizvodi(request):
    kolicine = {
        'stapovi':(Stapovi.objects.count(),str(Stapovi.objects.count())[-1]),
        'masinice':(Masinice.objects.count(),str(Masinice.objects.count())[-1]),
        'hrana':(Hrana.objects.count(),str(Hrana.objects.count())[-1]),
        'varalice':(Varalice.objects.count(),str(Varalice.objects.count())[-1]),
        'plovci':(Plovci.objects.count(),str(Plovci.objects.count())[-1]),
        'mamci':(Mamci.objects.count(),str(Mamci.objects.count())[-1]),
        'strune':(Strune.objects.count(),str(Strune.objects.count())[-1]),
        'udice':(Udice.objects.count(),str(Udice.objects.count())[-1]),
        'ostalo':(Ostalo.objects.count(),str(Ostalo.objects.count())[-1])
    }
    return render(request, 'home/proizvodi/proizvodi.html', kolicine)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def stapovi(request):
    stapovi = {
        'stapovi':Stapovi.objects.all()
    }
    return render(request, 'home/proizvodi/stapovi.html', stapovi)

def masinice(request):
    masinice = {
        'masinice':Masinice.objects.all()
    }
    return render(request, 'home/proizvodi/masinice.html', masinice)

def plovci(request):
    plovci = {
        'plovci':Plovci.objects.all()
    }
    return render(request, 'home/proizvodi/plovci.html', plovci)

def mamci(request):
    mamci = {
        'mamci':Mamci.objects.all()
    }
    return render(request, 'home/proizvodi/mamci.html', mamci)

def varalice(request):
    varalice = {
        'varalice':Varalice.objects.all()
    }
    return render(request, 'home/proizvodi/varalice.html', varalice)

def hrana(request):
    hrana = {
        'hrana':Hrana.objects.all()
    }
    return render(request, 'home/proizvodi/hrana.html', hrana)

def udice(request):
    udice = {
        'udice':Udice.objects.all()
    }
    return render(request, 'home/proizvodi/udice.html', udice)

def strune(request):
    strune = {
        'strune':Strune.objects.all()
    }
    return render(request, 'home/proizvodi/strune.html', strune)

def ostalo(request):
    ostalo = {
        'ostalo':Ostalo.objects.all()
    }
    return render(request, 'home/proizvodi/ostalo.html', ostalo)