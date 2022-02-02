from django.contrib import admin
from .models import Stapovi, Mamci, Masinice, Ostalo, Strune, Udice, Plovci, Hrana, Varalice

admin.site.register(Stapovi)
admin.site.register(Hrana)
admin.site.register(Plovci)
admin.site.register(Udice)
admin.site.register(Strune)
admin.site.register(Ostalo)
admin.site.register(Masinice)
admin.site.register(Mamci)
admin.site.register(Varalice)