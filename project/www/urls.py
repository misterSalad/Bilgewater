from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('linia/<int:pk>/', views.detail_linia, name='detail-linia'),
    path('rola/<int:pk>/', views.detail_rola, name='detail-rola'),
    path('bohater/<int:pk>/', views.detail_bohater, name='detail-bohater'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),

    path('linia/', views.linia_lista, name='linia-lista'),
    path('rola/', views.rola_lista, name='rola-lista'),
    path('bohater/', views.bohater_lista, name='bohater-lista'),
    path('dodaj-linia/', views.dodaj_linia, name='dodaj-linia'),
    path('dodaj-rola/', views.dodaj_rola, name='dodaj-rola'),
    path('dodaj-bohater/', views.dodaj_bohater, name='dodaj-bohater'),
    path('zapisano/', views.zapisano, name='zapisano'),
]