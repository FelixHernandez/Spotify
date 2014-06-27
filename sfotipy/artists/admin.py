#Se importa la libreria de administracion de django
from django.contrib import admin
#se importa la funcion para exportar a excel del archivo actions.py
from actions import export_as_excel
#Se importa el modelo de artista con sus respectivos atributos
from .models import Artist
#Se importa el modelo de Track para crear la relacion entre las tablas
from tracks.models import Track

#Se crea para que en la relacion existente se puedan agregar varios
#registros extra en la misma pagina de admin
class TrackInLine(admin.StackedInline):
	model=Track
	extra=2

#Se crea la clase para mostrar los diferentes elementos de manera
#personalizada en el admin de los artistas
class ArtistAdmin(admin.ModelAdmin):
	#Los campos que se mostraran de informacion
	list_display=('First_Name','Last_Name','Biography')
	#Los campos por los que se realiza la busqueda
	search_fields=('First_Name','Last_Name',)
	#Filtros para agregar canciones favoritas (relacion many to many)
	#filter_horizontal = ('favorite_songs',)
	filter_vertical = ('favorite_songs',)
	#las acciones que se pueden realizar en la vista
	actions = (export_as_excel,)
	#Se incluye la clase para agregar varios registros extra
	inlines=[TrackInLine,]

#Se registra en el admin la clase que se quiere mostrar del artista
admin.site.register(Artist,ArtistAdmin)