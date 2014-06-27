#se importa la libreria admin de django
from django.contrib import admin
#Se importa el modelo de album con sus atributos
from .models import Album

#Se crea una nueva clase la cual se mostrara en el administrador del album
class AlbumAdmin(admin.ModelAdmin):
	list_display=('Album_Title','Artist')
	search_fields=('Album_Title',)

#Se registra la clase anteriormente creada para que se muestre en el administrador
admin.site.register(Album,AlbumAdmin)