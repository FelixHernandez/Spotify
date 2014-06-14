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
		