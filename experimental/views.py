from django.shortcuts import render
from django.views.generic import ListView
from experimental.models import Place

# Create your views here.

class PlaceList(ListView):
    model = Place

