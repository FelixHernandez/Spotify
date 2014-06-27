from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Album
from rest_framework import viewsets



class AlbumViewSet(viewsets.ModelViewSet):
	model=Album