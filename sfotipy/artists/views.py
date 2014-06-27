from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Artist

class ArtistDetailView(DetailView):
	model=Artist
	context_object_name='artist'

	def get_template_names(self):
		return 'artist.html'

from rest_framework import viewsets

class ArtistViewSet(viewsets.ModelViewSet):
	model=Artist