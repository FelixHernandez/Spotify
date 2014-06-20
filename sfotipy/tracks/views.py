import json
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

def track_view(request,title):
	# try:
	# 	track=Track.objects.get(Title=title)
	# except Track.DoesNotExist:
	# 	raise Http404
	track=get_object_or_404(Track,Title=title)

	data={
		'Title': track.Title,
		'Order': track.Order,
		'Album': track.Album.Album_Title,
		'Artist':{
			'Name':track.Artist.First_Name,
			'Biography':track.Artist.Biography,
		}

	}

	json_data= json.dumps(data)

	#return HttpResponse(json_data, content_type='application/json')
	return render(request,'Track.html',{'Track': track})