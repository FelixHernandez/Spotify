import json
import time
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic.detail import DetailView
from .models import Track

class TrackDetailView(DetailView):
	model=Track
	context_object_name='fav_track'

	def get_template_names(self):
		return 'tracks.html'

#Crean el view set para la api
from rest_framework import viewsets
from .serializers import TrackSerializer
class TrackViewSet(viewsets.ModelViewSet):
	model=Track
	serializer_class=TrackSerializer
	filter_fields=('id',)
	paginate_by=1

from django.core.cache import cache
from django.views.decorators.cache import cache_page

# @cache_page(60)
def track_view(request,title):
	#Realiza la busqueda del archivo con el title que llega o envia un 404 si no lo encuentra
	#res=cache.get('data_%s'%title)
	#if res is None:
	track=get_object_or_404(Track,Title=title)
	# data={
	# 	'Title': track.Title,
	# 	'Order': track.Order,
	# 	'Album': track.Album.Album_Title,
	# 	'Artist':{
	# 		'Name':track.Artist.First_Name,
	# 		'Biography':track.Artist.Biography,
	# 	}

	# }		
		#cache.set('data_%s'%title,data)
	return render(request,'track.html',{'Track': track})

#Manera de enviar los datos con Json
	
	# json_data= json.dumps(data)
	#return HttpResponse(json_data, content_type='application/json')



	