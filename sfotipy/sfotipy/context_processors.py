#encoding:utf-8
from random import choice

frases=['Hola','Que Hace','Frase de Prueba']
from tracks.models import Track



def basico(request):
	tracks=Track.objects.all()
	track = None
	for t in tracks:
		if request.path == t.get_absolute_url():
			track=t
			break
				
			
	return{'Titulo': choice(frases),'Tracks':tracks,'track_ruta':track}