from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Artist
from .serializers import ArtistSerializer

class ArtistDetailView(DetailView):
	model=Artist
	context_object_name='artist'

	def get_template_names(self):
		return 'artist.html'


#Crean el view set para la api
from rest_framework import viewsets
from .serializers import ArtistSerializer
class ArtistViewSet(viewsets.ModelViewSet):
	model=Artist
	serializer_class=ArtistSerializer
	filter_fields=('id',)
	paginate_by=1