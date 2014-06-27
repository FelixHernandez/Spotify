#Se importa la clase de modelos de django
from django.db import models
#Se importa el modelo de artistas para la relacion entre las tablas
from artists.models import Artist

#se crea la clase de album con sus atributos respectivos
class Album(models.Model):
	Album_Title = models.CharField(max_length=255)
	Cover = models.ImageField(upload_to='albums')
	Artist = models.ForeignKey(Artist)

#se define la funcion unicode la cual se mostrara como predeterminado en el sitio
	def __unicode__(self):
		return self.Album_Title

