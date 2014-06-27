#Se importa la clase models de django
from django.db import models

#Se crea la clase artista con sus respectivos atributos
class Artist(models.Model):
	First_Name = models.CharField(max_length=255)
	Last_Name = models.CharField(max_length=255, blank=True)
	Biography = models.TextField(blank=True)
	favorite_songs = models.ManyToManyField('tracks.Track',blank=True,related_name='is_favorite_of')

	#se define la funcion unicode la cual sirve para hacer referencia a un objeto de manera predeterminada
	def __unicode__(self):
		return self.First_Name