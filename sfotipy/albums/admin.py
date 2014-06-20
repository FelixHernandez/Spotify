from django.contrib import admin

from .models import Album

class AlbumAdmin(admin.ModelAdmin):
	list_display=('Album_Title','Artist')

admin.site.register(Album,AlbumAdmin)