from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', { 'all_albums' : all_albums })
