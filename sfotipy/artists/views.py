from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic.detail import DetailView
from .models import Artist
from .serializers import ArtistSerializer

class ArtistDetailView(DetailView):
	model=Artist
	context_object_name='fav_artist'

	def get_template_names(self):
		return 'artists.html'

def artist_view(request,id):
	#Realiza la busqueda del archivo con el title que llega o envia un 404 si no lo encuentra
	artist=get_object_or_404(Artist,id=id)
	return render(request,'artist.html',{'Artist': artist})



#Crean el view set para la api
from rest_framework import viewsets
from .serializers import ArtistSerializer
class ArtistViewSet(viewsets.ModelViewSet):
	model=Artist
	serializer_class=ArtistSerializer
	filter_fields=('id',)
	paginate_by=1