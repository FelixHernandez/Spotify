from django.db import models
from artists.models import Artist

class Album(models.Model):
	Album_Title = models.CharField(max_length=255)
	Cover = models.ImageField(upload_to='albums')
	Artist = models.ForeignKey(Artist)

	def __str__(self):
		return self.Album_Title

