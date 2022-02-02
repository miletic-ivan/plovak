from django.db import models

class Stapovi(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='stapovi', blank=True)
    kolicina = models.PositiveSmallIntegerField()
    duzina = models.FloatField()
    tezina_stapa = models.PositiveSmallIntegerField()
    tezina_bacanja = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Stapovi'

class Masinice(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='masinice', blank=True)
    kolicina = models.PositiveSmallIntegerField()
    tezina = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Masinice'

class Hrana(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='hrana', blank=True)
    tezina = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Hrana'

class Udice(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='hrana', blank=True)
    velicina = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Udice'


class Varalice(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='varalice', blank=True)
    duzina = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Varalice'

class Plovci(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='plovci', blank=True)
    duzina = models.PositiveSmallIntegerField(blank=True)
    ampula = models.BooleanField(blank=True)

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Plovci'

class Ostalo(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='ostalo', blank=True)
    opis = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Ostalo'

class Mamci(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='mamci', blank=True)

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Mamci'

class Strune(models.Model):
    naziv = models.CharField(max_length=40)
    slika = models.ImageField(upload_to='strune', blank=True)
    duzina = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.naziv

    class Meta():
        verbose_name_plural = 'Strune'