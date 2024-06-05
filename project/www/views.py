from django.shortcuts import render, get_object_or_404
from .models import Linia, Rola, Bohater

from .forms import LiniaForm, RolaForm, BohaterForm
from django.http import HttpResponseRedirect


linia = Linia.objects.all()
rola = Rola.objects.all()
bohater = Bohater.objects.all()


# Create your views here.
def index(request):

    return render(request, 'www/index.html', {
        'linia': linia,
        'rola': rola,
        'bohater': bohater,
        })

def bootstrap(request):

    return render(request, 'www/bootstrap.html', {
        'bohater': bohater
        })

def detail_linia(request, pk):
    linia = get_object_or_404(Linia, pk=pk)
    return render(request, 'www/detail-linia.html', {
        'linia': linia,
        'pk':pk
        })

def detail_rola(request, pk):
    rola = get_object_or_404(Rola, pk=pk)
    return render(request, 'www/detail-rola.html', {
        'rola': rola,
        'pk':pk
        })

def detail_bohater(request, pk):
    bohater = get_object_or_404(Bohater, pk=pk)
    return render(request, 'www/detail-bohater.html', {
        'bohater': bohater,
        'pk':pk
        })

def linia_lista(request):
    return render(request, 'www/linia.html', {
        'linia': linia
        })

def rola_lista(request):
    return render(request, 'www/rola.html', {
        'rola': rola
        })

def bohater_lista(request):
    return render(request, 'www/bohater.html', {
        'bohater': bohater
        })

def dodaj_linia(request):
    if request.method == 'POST':
        form = LiniaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = LiniaForm()

    return render(request, 'www/dodaj-linia.html', {'form': form})


def dodaj_rola(request):
    if request.method == 'POST':
        form = RolaForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = RolaForm()

    return render(request, 'www/dodaj-rola.html', {'form': form})


def dodaj_bohater(request):
    if request.method == 'POST':
        form = BohaterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = BohaterForm()

    return render(request, 'www/dodaj-bohater.html', {'form': form})


def zapisano(request):
    return render(request, 'www/zapisano.html')