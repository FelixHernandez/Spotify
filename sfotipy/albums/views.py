from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Album

class AlbumDetailView(DetailView):
	model=Album
	context_object_name='fav_album'

	def get_template_names(self):
		return 'album.html'




#Crean el view set para la api
from rest_framework import viewsets
from .serializers import AlbumSerializer
class AlbumViewSet(viewsets.ModelViewSet):
	model=Album
	serializer_class=AlbumSerializer
	paginate_by=2