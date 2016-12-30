from django.db import models

# Create your models here.
class Album(models.Model): # every class it has to inherites from models.Model
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=250)
	genre = models.CharField(max_length=250)
	album_logo = models.FileField(max_length=250)

	def __str__(self):
		return self.album_title + ' - ' + self.artist


class Song(models.Model): # every class it has to inherites from models.Model
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=250)
	song_title = models.CharField(max_length=250)

	def __str__(self):
		return self.song_title
