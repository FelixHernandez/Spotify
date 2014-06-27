#se importa la clase admin de django
from django.contrib import admin
#se importa la funcion para exportar datos a excel del archivo actions.py
from actions import export_as_excel
#se importa la clase tracks con sus respectivos atributos
from .models import Track

#Se crea la clase para mostrar de manera personalizada en el admin
class TrackAdmin(admin.ModelAdmin):
	#Los campos que se mostraran
	list_display = ('Title','Artist','Order','player','es_beatles')
	#los campos por los que se filtraran
	list_filter=('Artist','Album')
	#Los campos por los que se realizara la busqueda
	search_fields=('Title','Artist__First_Name')
	#los datos que se pueden evitar (la primera columna no se permite)
	list_editable=('Order',)
	#las acciones que se muestran en el admin para manejar los datos
	actions = (export_as_excel,)
	#Para editar por medio de una busqueda
	raw_id_fields=('Artist',)


	#se define una funcion booleana en donde se muestra la respuesta como un icono
	#(Hay que incluirlo en el list_display)
	def es_beatles(self,obj):
		return obj.Artist.First_Name=='The Beatles'
	es_beatles.boolean=True

#se registra la clase en el admin para que se muestre
admin.site.register(Track,TrackAdmin)