from django.contrib import admin
from actions import export_as_excel
from .models import Artist
from tracks.models import Track
class TrackInLine(admin.StackedInline):
	model=Track
	extra=2

class ArtistAdmin(admin.ModelAdmin):
	list_display=('First_Name','Last_Name','Biography')
	search_fields=('First_Name','Last_Name',)
	#filter_horizontal = ('favorite_songs',)
	filter_vertical = ('favorite_songs',)
	actions = (export_as_excel,)
	inlines=[TrackInLine,]


admin.site.register(Artist,ArtistAdmin)