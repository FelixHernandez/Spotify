from django.contrib import admin
from actions import export_as_excel
from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('Title','Artist','Order','player','es_beatles')
	list_filter=('Artist','Album')
	search_fields=('Title','Artist__First_Name')
	list_editable=('Order',)
	actions = (export_as_excel,)
	raw_id_fields=('Artist',)

	def es_beatles(self,obj):
		return obj.Artist.First_Name=='The Beatles'
	es_beatles.boolean=True

admin.site.register(Track,TrackAdmin)