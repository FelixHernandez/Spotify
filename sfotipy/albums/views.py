from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Album


from rest_framework import viewsets
from .serializers import AlbumSerializer
class AlbumViewSet(viewsets.ModelViewSet):
	model=Album
	serializer_class=AlbumSerializer
	paginate_by=2