from django.urls import path

from . import views

urlpatterns = [
    path('daftar/', views.daftar),
    path('anggota/', views.anggota),
    path('', views.anggota),
]