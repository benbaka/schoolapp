from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from experimental.models import Place
from django.utils import timezone
# Create your views here.


class PlaceList(ListView):
    model = Place


class PlaceDetailView(DetailView):

    model = Place


class PlaceCreate(CreateView):
    model = Place

    #def get_success_url(self):
    #    return reverse('place', kwargs={'pk': self.object.pk})
