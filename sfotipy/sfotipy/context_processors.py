#encoding:utf-8
#crea una variable aleatoria
from random import choice
#una lista con frases diferentes
frases=['Hola','Que Hace','Frase de Prueba']
#Se importa el modelo Track
from tracks.models import Track
from artists.models import Artist
#Se crea la funcion basico
def basico(request):
	#Se obtienen los tracks que existan registrados
	tracks=Track.objects.all()
	#Variable que devuelve el track que se encuentra seleccionado
	selected_track = None
	#ciclo for para comparar cual es el track que se muestra en el url
	for t in tracks:
		if request.path == t.get_absolute_url():
			selected_track=t
			break			
	#Se envian las diferentes variables que se mostraran en el template
	return{'Titulo': choice(frases),'Tracks':tracks,'selected_track':selected_track}

def basico(request):
	artists=Artist.objects.all()
	selected_artist=None
	for a in artists:
		print a
		if request.path==a.get_absolute_url():
			selected_artist=a
			break
	return{'Titulo':'Artistas','Artists':artists,'selected_artist':selected_artist}