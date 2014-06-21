from django.db import models

class Artist(models.Model):
	First_Name = models.CharField(max_length=255)
	Last_Name = models.CharField(max_length=255, blank=True)
	Biography = models.TextField(blank=True)
	favorite_songs = models.ManyToManyField('tracks.Track',blank=True,related_name='is_favorite_of')

	def __unicode__(self):
		return self.First_Name