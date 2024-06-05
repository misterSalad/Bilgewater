from django.db import models

class Linia(models.Model):
    nazwa = models.CharField(max_length=200)
    ikonka = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nazwa

class Rola(models.Model):
    nazwa = models.CharField(max_length=250)
    emblemat = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nazwa

class Bohater(models.Model):
    imie = models.CharField(max_length=100)
    przydomek = models.CharField(max_length=100)
    rola = models.ManyToManyField(Rola)
    linia = models.ManyToManyField(Linia)
    zdjecie = models.ImageField(upload_to='images')

    def __str__(self):
        return self.imie + ", " + self.przydomek