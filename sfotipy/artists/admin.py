from django.contrib import admin

from .models import Artist
class ArtistAdmin(admin.ModelAdmin):
	list_display=('First_Name','Last_Name','Biography')
admin.site.register(Artist,ArtistAdmin)