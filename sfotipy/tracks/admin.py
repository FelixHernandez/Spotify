from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('Title','Artist','Order','player','es_beatles')
	list_filter=('Artist','Album')
	search_fields=('Title','Artist__First_Name')
	list_editable=('Order',)

	def es_beatles(self,obj):
		return obj.Artist.First_Name=='The Beatles'
	es_beatles.boolean=True
admin.site.register(Track,TrackAdmin)

