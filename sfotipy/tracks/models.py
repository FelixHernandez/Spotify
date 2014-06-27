from django.db import models
from artists.models import Artist
from albums.models import Album
# Create your models here.
class Track(models.Model):
	Title = models.CharField(max_length=255)
	Order = models.PositiveIntegerField()
	Track_File = models.FileField(upload_to='tracks')
	Album = models.ForeignKey(Album)
	Artist = models.ForeignKey(Artist)


	def get_absolute_url(self):
		return '/tracks/%s/'%self.Title


#Funcion de Reproductor multimedia
	def player(self):
		return """
			<audio controls>
				<source src="%s" type="audio/mpeg">
				Tu Navegador no soporta el formato
			</audio>
		"""% self.Track_File.url
	player.allow_tags=True
	player.admin_order_field='Track_File'
			
	def __unicode__(self):
		return self.Title