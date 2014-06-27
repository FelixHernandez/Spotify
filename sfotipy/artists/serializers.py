from rest_framework import serializers
from .models import Artist
class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	es_beatles1=serializers.SerializerMethodField('es_beatles2')
	
	def es_beatles2(self,obj):
		return obj.es_beatles()

	class Meta:
		model=Artist
		fields=('id','First_Name','Last_Name','es_beatles1',)